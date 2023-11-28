# Project Setup Guide


## Overview

This guide provides step-by-step instructions to set up the project, run the server, execute tests, understand project requirements, and review highlighted changes.


## Tech Stack

### Backend

- **Python:** Core programming language for server-side logic.
- **Flask:** Web framework used for building the backend application.
- **SQLAlchemy:** Python SQL toolkit and Object-Relational Mapping (ORM) used for database management.
- **PyJWT:** Python implementation of JSON Web Tokens (JWT) for user authentication.
- **PostgreSQL:** Relational database management system utilized as the backend database.


### Backend Setup

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd shopping-store-api
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Unix/Mac
    venv\Scripts\activate  # For Windows
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Flask application:**
    ```bash
    flask run
    ```

## Endpoints

The API supports the following endpoints:

- `GET /login`: Login using Auth0 authentication.
- `GET /logout`: Logout using Auth0.
- `GET /products`: Retrieve all products.
- `GET /customers/<int:customer_id>`: Retrieve a specific customer.
- `POST /item`: Create a new item.
- ... (and more)

## Roles and Permissions

- **dev - public**:
  - Limited access for basic functionalities.
- **product admin role**:
  - Access to product-related functionalities.
- **Admin**:
  - Full access to all functionalities.

## Postman Collection

Use the [shopping-api.postman_collection.json](./shopping%20-api.postman-v2_collection.json) file to test endpoints in Postman.

## JWT Tokens

- **Product Role JWT**: [Token required]
- **Admin JWT**: [Token required]

## Testing

The [test_end_points.py](./test_end_points.py) file contains unit tests for success and failure scenarios for each endpoint.

## Database Design
See [database.png](./database-design/database.png) for the database design.
