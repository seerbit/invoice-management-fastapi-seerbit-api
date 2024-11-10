# Invoice Management App with FastAPI and SeerBit API Integration

**Welcome to the Invoice Management App!** 

This project showcases a streamlined approach to creating, managing, and sending invoices through FastAPI and SeerBit API, with MongoDB as a backend database. With its core in simplicity and scalability, this app is designed for developers interested in building financial solutions that require secure, efficient payment and invoicing functionalities.

## Features

	•	Invoice Creation: Quickly generate invoices with key details, including client information, due dates, and itemized amounts.
	•	Invoice Retrieval: Retrieve stored invoices by ID for easy review and updates.
	•	Invoice Sending: Send invoices directly via SeerBit, leveraging their API for smooth, real-time communication with clients.

## Tech Stack

	•	FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
	•	MongoDB: Used for storing and managing invoice data.
	•	SeerBit API: Provides secure payment and invoicing capabilities for financial integrations.

## Getting Started

Prerequisites

	•	Python 3.8 or higher
	•	MongoDB instance (local or hosted)
	•	SeerBit API credentials (API URL, Public Key, Encrypted Key)
	•	.env file with the following keys:

```
DATABASE_URI="your_mongo_db_uri"
SEERBIT_API_URL="seerbit_api_base_url"
SEERBIT_ENCRYPTED_KEY="seerbit_encrypted_key"
SEERBIT_SEND_INVOICE_API="seerbit_send_invoice_url"
PUBLIC_KEY="your_public_key"
```

## Libraries & Tools Used

	1.	**FastAPI**
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python. It is ideal for building applications that require high-performance requests. In this app, FastAPI is used to create RESTful endpoints that manage invoices.
	2.	Pydantic
Used for data validation and serialization. Pydantic is used here to define the Invoice model that validates incoming data for invoice creation.
	3.	Requests
A simple and elegant HTTP library used to make requests to the SeerBit API for creating and sending invoices. We use it to send POST and GET requests to the SeerBit API for invoice management.
	4.	PyMongo
This is the official Python driver for MongoDB. It’s used to interact with a MongoDB database for storing and retrieving invoice data in this app.
	5.	BSON
BSON (Binary JSON) is used for handling MongoDB’s unique ObjectId format, which is used to query documents in the invoices collection.
	6.	Dotenv
We use this to load sensitive environment variables (like API keys and database URLs) from a .env file, ensuring security and easy configuration.

## Installation

	1.	Clone the repository:

git clone https://github.com/seerbit/invoice-management-fastapi-seerbit-api.git


	2.	Install dependencies:

pip install -r requirements.txt


	3.	Set up environment variables: Create a .env file in the root directory and add the required keys (as shown above).
	4.	Start the FastAPI server:

```
"fastapi[standard]"
```


	5.	Access the interactive API docs:
Navigate to http://127.0.0.1:8000/docs to explore and test the API endpoints using FastAPI’s Swagger UI.

## API Endpoints

1. Create Invoice

	•	Endpoint: /invoice/create
	•	Method: POST
	•	Request: JSON payload with invoice details (order number, amount, client info, etc.)
	•	Response: Success message with MongoDB invoice ID.

2. Retrieve Invoice

	•	Endpoint: /invoice/{invoice_id}
	•	Method: GET
	•	Response: Returns the invoice details if found.

3. Send Invoice

	•	Endpoint: /invoice/send/{invoice_id}
	•	Method: POST
	•	Description: Custom endpoint that triggers SeerBit API to send an invoice to the client.

## How It Works

	1.	Invoice Creation: Invoice data is validated and sent to the SeerBit API. If successful, the invoice is stored in MongoDB.
	2.	Invoice Retrieval: Invoices can be fetched using their unique IDs stored in MongoDB.
	3.	Send Invoice: Sends the created invoice to clients via SeerBit’s send API, notifying them of pending payments.

## Notes

	•	Ensure your SeerBit API credentials are correctly set in your .env file for smooth integration.
	•	MongoDB URI should allow external connections if using a cloud-based database.

## Contributions

This project is open-source and welcomes contributions! Fork, star, and submit pull requests for improvements.

This README provides a clear overview of the application and guides users on setup, functionality, and contribution. Enjoy building and exploring with FastAPI and SeerBit!# invoice-management-fastapi-seerbit-api
# invoice-management-fastapi-seerbit-api
