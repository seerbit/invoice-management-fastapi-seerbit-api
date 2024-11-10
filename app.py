from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import pymongo
from bson import ObjectId
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# MongoDB setup
database_url = os.getenv('DATABASE_URI')
client = pymongo.MongoClient(database_url)
db = client["invoice_db"]
invoices_collection = db["invoices"]

# SEERBIT API endpoint and authorization
seerbit_api_url = os.getenv('SEERBIT_API_URL')
seerbit_encrypted_key = os.getenv('SEERBIT_ENCRYPTED_KEY')
seerbit_api_send_invoice_url = os.getenv('SEERBIT_SEND_INVOICE_API')

class Invoice(BaseModel):
    order_no: str
    due_date: str
    currency: str
    receivers_name: str
    customer_email: str
    amount: int
    service_description: str
    invoice_items: list

public_key = os.getenv('PUBLIC_KEY')

# 1. Create Invoice Endpoint
@app.post("/invoice/create")
def create_invoice(invoice: Invoice):
    invoice_data = {
        "publicKey": public_key,
        "orderNo": invoice.order_no,
        "dueDate": invoice.due_date,
        "currency": invoice.currency,
        "amount": invoice.amount,
        "serviceDescription": invoice.service_description,
        "receiversName": invoice.receivers_name,
        "customerEmail": invoice.customer_email,
        "invoiceItems": invoice.invoice_items,
    }

    headers = {
        "Authorization": f"Bearer {seerbit_encrypted_key}",
        "Content-Type": "application/json"
    }

    # Send POST request to SEERBIT API
    response = requests.post(f"{seerbit_api_url}", json=invoice_data, headers=headers)

    if response.status_code == 200:  # Check for success status
        # Insert invoice data into MongoDB
        invoice_id = invoices_collection.insert_one(invoice_data).inserted_id
        return {"message": "Invoice created successfully", "invoice_id": str(invoice_id)}
    else:
        raise HTTPException(status_code=response.status_code, detail=f"Error creating invoice: {response.text}")

# 2. Retrieve Invoice Endpoint
@app.get("/invoice/{invoice_id}")
def retrieve_invoice(invoice_id: str):
    invoice = invoices_collection.find_one({"_id": ObjectId(invoice_id)})
    if invoice:
        return {
            "client_name": invoice.get("receiversName"),
            "service_description": invoice.get("serviceDescription"),
            "amount": invoice.get("amount"),
            "due_date": invoice.get("dueDate"),
            "client_email": invoice.get("customerEmail"),
        }
    else:
        raise HTTPException(status_code=404, detail="Invoice not found")

# 3. Send Invoice Endpoint
# Custom POST endpoint for sending invoices
@app.post("/invoice/send/{invoice_id}")
async def send_invoice(invoice_id: str):
    # Fetch invoice data from MongoDB
    invoice = invoices_collection.find_one({"_id": ObjectId(invoice_id)})
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    # SEERBIT API expects a GET request, so we make a GET request to the API endpoint
    api_url = f"{seerbit_api_send_invoice_url}/{public_key}/send/{invoice_id}"

    # Prepare headers for the request
    headers = {
        "Authorization": f"Bearer {seerbit_encrypted_key}",
        "Content-Type": "application/json"
    }

    # Make the GET request to SeerBit API to send the invoice
    response = requests.get(api_url, headers=headers)

    # Check response from SeerBit
    if response.status_code == 200:
        return {"message": "Invoice sent successfully via custom endpoint"}
    else:
        raise HTTPException(status_code=response.status_code, detail=f"Failed to send invoice: {response.text}")
    
