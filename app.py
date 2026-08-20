from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="ITGC Compliance & Evidence API", version="1.0")

# Shared data store or connection layer
evidence_registry = [
    {"request_id": "REQ-001", "control_id": "AC-1", "framework": "NIST SP 800-53", "status": "Open"}
]

class EvidenceModel(BaseModel):
    request_id: str
    control_id: str
    framework: str
    status: str

@app.get("/api/v1/evidence", response_model=List[EvidenceModel])
def get_evidence():
    """External systems can call this GET endpoint to pull active audit items into their pipelines."""
    return evidence_registry

@app.post("/api/v1/evidence")
def push_evidence(item: EvidenceModel):
    """External scanners or ticketing tools can POST new evidence requests directly here."""
    evidence_registry.append(item.dict())
    return {"status": "success", "added": item}
