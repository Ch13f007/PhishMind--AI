from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import init_db
from backend.routes import employees, campaigns, tracking

app = FastAPI(
    title="PhishMind AI",
    description="Adaptive AI-Powered Phishing Awareness for African SMEs",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    init_db()
    print("✅ PhishMind AI database ready!")


@app.get("/")
def root():
    return {"message": "PhishMind AI is running 🎣"}


@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "0.1.0"}


app.include_router(employees.router, prefix="/api/employees", tags=["Employees"])
app.include_router(campaigns.router, prefix="/api/campaigns", tags=["Campaigns"])
app.include_router(tracking.router, prefix="/api/track", tags=["Tracking"])