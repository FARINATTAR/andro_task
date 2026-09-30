# E-commerce Admin API

A backend API for managing an e-commerce admin system.

Built with FastAPI, SQLAlchemy and SQLite. Currently includes database setup
and Brand CRUD operations with validation and soft delete.

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
├── main.py            # Application entry point
├── database.py        # Database connection and session setup
│
├── models/
│   └── brand.py       # Brand database model
│
├── schemas/
│   └── brand.py       # Request and response schemas
│
├── services/
│   └── brand_service.py   # Business logic
│
└── routers/
    └── brand.py       # API route definitions
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/FARINATTAR/andro_task.git
cd ecommerce-admin-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate on Git Bash:

```bash
source venv/Scripts/activate
```

Activate on CMD:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn app.main:app --reload
```

The API will run at `http://127.0.0.1:8000`

## Database

The project uses SQLite. The database file `ecommerce.db` is created automatically
when the application starts.

SQLAlchemy handles table creation on startup through `Base.metadata.create_all()`.

## Brand API

### Endpoints

| Method   | Endpoint              | Status Code | Description         |
|----------|-----------------------|-------------|---------------------|
| `POST`   | `/brands/`            | 201         | Create a brand      |
| `GET`    | `/brands/`            | 200         | Get all active brands |
| `GET`    | `/brands/{brand_id}`  | 200         | Get a single brand  |
| `PATCH`  | `/brands/{brand_id}`  | 200         | Update a brand      |
| `DELETE` | `/brands/{brand_id}`  | 204         | Soft delete a brand |

### Brand Fields

| Field         | Type    | Required | Description                    |
|---------------|---------|----------|--------------------------------|
| `name`        | string  | Yes      | Brand name (max 100 chars)     |
| `slug`        | string  | Yes      | URL-friendly identifier        |
| `description` | string  | No       | Brand description              |
| `logo_url`    | string  | No       | URL to brand logo              |
| `is_active`   | boolean | No       | Whether brand is active (default: true) |

### Validation Rules

- Brand name is required and cannot exceed 100 characters.
- Slug must be lowercase and can only contain letters, numbers and hyphens.
- Brand name and slug must be unique.
- Deleted brands are excluded from normal GET responses.

Valid slug examples:

```
nike
nike-sports
nike-2026
```

Invalid slug examples:

```
Nike           # uppercase not allowed
Nike Sports    # spaces not allowed
nike_sports    # underscores not allowed
```

### Example Requests

**Create a brand:** `POST /brands/`

```json
{
  "name": "Nike",
  "slug": "nike",
  "description": "Just Do It",
  "logo_url": "https://example.com/nike-logo.png",
  "is_active": true
}
```

**Update a brand (partial):** `PATCH /brands/1`

```json
{
  "name": "Nike Inc."
}
```

## Soft Delete

Brands are not permanently removed from the database. When a brand is deleted,
the `is_deleted` field is set to `true`. This keeps the record in the database
while hiding it from normal API responses.

## API Documentation

Swagger UI is available at:

```
http://127.0.0.1:8000/docs
```

The API can be tested directly from the Swagger interface.

## Development Note

AI assistance was used during the development of this project. The generated
implementation was reviewed and studied to understand the architecture,
database setup, validation, CRUD flow and business logic.