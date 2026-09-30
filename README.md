# E-commerce Admin API

A simple backend API for managing an e-commerce admin system.

The project is built using FastAPI, SQLAlchemy and SQLite. It currently includes
database setup and Brand CRUD operations with validation and soft delete.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn

## Project Structure

```text
app/
├── main.py
├── database.py
│
├── models/
│   └── brand.py
│
├── schemas/
│   └── brand.py
│
├── services/
│   └── brand_service.py
│
└── routers/
    └── brand.py
Setup
1. Clone the repository
git clone <your-repository-url>
cd ecommerce-admin-api
2. Create a virtual environment
python -m venv venv

Activate it on Git Bash:

source venv/Scripts/activate
3. Install dependencies
pip install fastapi uvicorn sqlalchemy pydantic
4. Run the application
uvicorn app.main:app --reload

The API will run at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs

Database

The project currently uses SQLite.

The database file is:

ecommerce.db

SQLAlchemy creates the database tables when the application starts.

Brand API

The current API supports:

Method	Endpoint	Description
POST	/brands/	Create a brand
GET	/brands/	Get all active brands
GET	/brands/{brand_id}	Get a single brand
PATCH	/brands/{brand_id}	Update a brand
DELETE	/brands/{brand_id}	Soft delete a brand
Brand Validation
Brand name is required.
Brand name can have a maximum of 100 characters.
Slug must be lowercase.
Slug can contain letters, numbers and hyphens.
Brand name and slug must be unique.
Deleted brands are not returned by the normal GET APIs.

Example slug:

nike
nike-sports
nike-2026

Invalid examples:

Nike
Nike Sports
nike_sports
Soft Delete

Brands are not permanently removed from the database.

When a brand is deleted:

is_deleted = True

This keeps the record in the database while hiding it from normal API responses.

API Documentation

Swagger UI is available at:

http://127.0.0.1:8000/docs

The API can be tested directly from Swagger.

Development Note

AI assistance was used during the development of this project. The generated
implementation was reviewed and studied to understand the architecture,
database setup, validation, CRUD flow and business logic.