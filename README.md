# CRM RESTful API Project

A CRM Django-based REST API project secured with OAuth2 using Django OAuth Toolkit.

## 🚀 Features

- RESTful API at `/api/v1/`
- Django Admin panel
- Configurable via `config/settings/base.py` file

---

## 🛠️ Prerequisites

- Python 3.10.+
- MySQL 8+
- pip
- (Optional but recommended) `pip install virtualenv`
- Required libraries in `requirements/development.txt`
---

## 📁 Project Structure
```
crm_backend/
│
├── config/             # Django settings
|   └──  base.py        # Store base settings
├── crm/                # CRM app
|   ├── api/            # Contains APIs
|   ├── migrations/     # Migration files
|   ├── models/         # Entities
|   ├── services/       # Service functions
|   ├── static/         # Contains upload file (for dev purpose)
|   ├── templates/      # Email templates and overrided admin templates
|   ├── tests/          # Unit tests
|   ├── utils/
|   ├── admin.py        # Admin management
|   └── apps.py
├── .env                # Store configuration variables (rename .env_example)
├── manage.py
├── requirements/
|   ├── development.txt # Store required libraries
|   └── production.txt
└── README.md
```

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ducbang1510/crm_backend.git
cd crm_backend
```

### 2. Create and start virtual environment
```bash
virtualenv venv               # OR python -m venv venv
source venv/bin/activate      # Windows OS: venv\Scripts\activate
```

### 3. Install all required libraries
```bash
pip install -r requirements/development.txt
```

### 4. Run migration to initialize tables
Note: Create your schema in database first 
```bash
python manage.py makemigrations
python manage.py migrate oauth2_provider
python manage.py migrate
```

### 5. Create superuser
Register one superuser for OAuth2 setup and admin view
```bash
python manage.py createsuperuser
```

### 6. Start app
```bash
python manage.py runserver
```
Visit: http://localhost:8000/crm/admin/ (admin view - need staff/superuser account)

---

## 🔐 OAuth2 Setup
Create new OAuth2 app http://127.0.0.1:8000/o/applications/register/

### Under Applications, create a new OAuth2 app:

1. Name: Put your app name (e.g. CRM_APP)

2. Copy the Client ID and Client Secret to use after

3. Enable Hash Client Secret option (recommend)

4. Client type: Confidential (server-side), Public (for SPAs/mobile apps)

5. Authorization grant type: 
   1. Resource owner password-based (password)
   2. Implicit (implicit)

6. Algorithm: No OIDC support

7. Other fields can keep empty

---

## Generate SECRET_KEY for .env
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```