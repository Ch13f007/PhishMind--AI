from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import Employee, Campaign, ClickEvent
from backend.services.ai_generator import (
    generate_phishing_email,
    generate_smishing_message,
    generate_awareness_training
)
from pydantic import BaseModel
from datetime import datetime
from typing import List

router = APIRouter()


class SimulationRequest(BaseModel):
    employee_id: int
    campaign_id: int


class ClickEventResponse(BaseModel):
    id: int
    employee_id: int
    campaign_id: int
    clicked: bool
    training_shown: bool

    class Config:
        from_attributes = True


@router.post("/simulate")
def generate_simulation(request: SimulationRequest, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == request.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    campaign = db.query(Campaign).filter(Campaign.id == request.campaign_id).first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    # Create a click event record
    click_event = ClickEvent(
        employee_id=employee.id,
        campaign_id=campaign.id,
        clicked=False
    )
    db.add(click_event)
    db.commit()
    db.refresh(click_event)

    # Generate simulation
    tracking_url = f"http://127.0.0.1:8000/api/track/click/{click_event.id}"

    if campaign.simulation_type == "email":
        simulation = generate_phishing_email(
            employee_name=employee.name,
            role=employee.role,
            industry=employee.industry
        )
        simulation["body"] = simulation["body"].replace("{tracking_url}", tracking_url)
    else:
        simulation = generate_smishing_message(
            employee_name=employee.name,
            role=employee.role,
            industry=employee.industry
        )
        simulation["message"] = simulation["message"].replace("{tracking_url}", tracking_url)

    return {
        "click_event_id": click_event.id,
        "employee": employee.name,
        "simulation_type": campaign.simulation_type,
        "simulation": simulation,
        "tracking_url": tracking_url
    }


@router.get("/click/{click_event_id}", response_class=HTMLResponse)
def track_click(click_event_id: int, db: Session = Depends(get_db)):
    click_event = db.query(ClickEvent).filter(ClickEvent.id == click_event_id).first()
    if not click_event:
        raise HTTPException(status_code=404, detail="Invalid link")

    # Log the click
    if not click_event.clicked:
        click_event.clicked = True
        click_event.clicked_at = datetime.utcnow()

        # Update employee risk score
        employee = db.query(Employee).filter(Employee.id == click_event.employee_id).first()
        employee.risk_score = min(100.0, employee.risk_score + 25.0)

        click_event.training_shown = True
        db.commit()

    # Generate awareness training
    from backend.models import Campaign
    campaign = db.query(Campaign).filter(Campaign.id == click_event.campaign_id).first()
    simulation = generate_phishing_email(
        employee_name="",
        role="",
        industry=campaign.industry
    )
    training_html = generate_awareness_training(simulation["red_flags"])
    return HTMLResponse(content=training_html)


@router.get("/results/{campaign_id}", response_model=List[ClickEventResponse])
def get_campaign_results(campaign_id: int, db: Session = Depends(get_db)):
    events = db.query(ClickEvent).filter(ClickEvent.campaign_id == campaign_id).all()
    return events