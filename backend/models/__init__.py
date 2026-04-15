from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    risk_score = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

    click_events = relationship("ClickEvent", back_populates="employee")


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    simulation_type = Column(String, nullable=False)  # email or sms
    industry = Column(String, nullable=False)
    status = Column(String, default="draft")  # draft, active, completed
    created_at = Column(DateTime, default=datetime.utcnow)

    click_events = relationship("ClickEvent", back_populates="campaign")


class ClickEvent(Base):
    __tablename__ = "click_events"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    clicked = Column(Boolean, default=False)
    clicked_at = Column(DateTime, nullable=True)
    training_shown = Column(Boolean, default=False)

    employee = relationship("Employee", back_populates="click_events")
    campaign = relationship("Campaign", back_populates="click_events")