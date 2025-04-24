from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import JSONResponse
from uuid import uuid4
from typing import Dict

from models import Receipt
from processor import calculate_points

app = FastAPI()

# In-memory store for receipts and their points
receipt_store: Dict[str, Receipt] = {}

@app.get("/")
def read_root():
    return {"message": "Receipt Processor is running"}

@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    receipt_id = str(uuid4())
    receipt_store[receipt_id] = receipt
    return JSONResponse(content={"id": receipt_id})

@app.get("/receipts/{receipt_id}/points")
def get_receipt_points(receipt_id: str = Path(...)):
    receipt = receipt_store.get(receipt_id)
    if not receipt:
        raise HTTPException(status_code=404, detail="No receipt found for that ID.")
    points = calculate_points(receipt)
    return {"points": points}