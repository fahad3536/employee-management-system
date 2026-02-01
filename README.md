# Employee Management System (Dynamic Forms)

A full-stack **Employee Management System** built using **Django, Django
REST Framework, JWT authentication**, and a **lightweight HTML +
JavaScript (Axios)** frontend.

The system supports **dynamic form creation**, **employee CRUD
operations**, and **JWT-based authentication**, all exposed via REST
APIs and consumed using AJAX.

------------------------------------------------------------------------

## 🚀 Features

### 🔐 Authentication & Profile

-   User Registration
-   JWT Login (Access & Refresh Tokens)
-   Change Password
-   View & Update Profile

### 🧩 Dynamic Form Builder

-   Create multiple dynamic forms
-   Add/edit fields dynamically
-   Supported field types:
    -   Text
    -   Number
    -   Date
    -   Email
    -   Password
    -   Textarea
-   Field ordering (drag & drop ready via order index)

### 👤 Employee Management

-   Create employees using dynamic forms
-   Store dynamic data using JSONField
-   Full CRUD operations
-   Dynamic validation based on form schema
-   Search employees by dynamic fields

### 🌐 Frontend (AJAX-based)

-   Plain HTML + JavaScript
-   Axios for API communication
-   JWT stored in localStorage
-   Dynamic form rendering

------------------------------------------------------------------------

## 🛠 Tech Stack

Backend: Python, Django, Django REST Framework\
Auth: JWT (SimpleJWT)\
Database: SQLite\
Frontend: HTML, JavaScript\
HTTP Client: Axios

------------------------------------------------------------------------

## 📁 Project Structure

    core/
    ├── accounts/
    ├── employees/
    ├── forms_builder/
    ├── core/
    └── manage.py
    frontend/

------------------------------------------------------------------------

## ⚙️ Setup Instructions

``` bash
git clone https://github.com/fahad3536/employee-management-system
cd core
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers
python manage.py migrate
python manage.py runserver
```

------------------------------------------------------------------------

## 🔗 API Overview

Authentication: - POST /api/accounts/register/ - POST
/api/accounts/login/

Dynamic Forms: - POST /api/forms/forms/ - GET /api/forms/forms/{id}/

Employees: - POST /api/employees/employees/ - GET
/api/employees/employees/list/ - PUT
/api/employees/employees/{id}/update/ - DELETE
/api/employees/employees/{id}/

------------------------------------------------------------------------

## 🧪 Postman Collection

A complete Postman collection is included for all APIs.

------------------------------------------------------------------------

## 🙌 Author

**Fahad Nawaz**\
Senior Python / Django Developer
