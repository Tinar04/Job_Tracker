# 🎯 JobTracker

> A full stack web application to track your job applications — built with Django, MySQL, and Bootstrap.

---

## 📌 About The Project

JobTracker is a personal job application tracking system built during my own placement process. Instead of maintaining a messy notes app or spreadsheet, I built a real web application to track every company I applied to, the status of each application, interview feedback, and more.

This project demonstrates full stack development using Python (Django) on the backend, MySQL as the database, and Bootstrap for the frontend.

---

## ✨ Features

- 📋 Add job applications with company name, role, status, location, salary, source and notes
- 🔄 Track application status — Applied, Under Review, Shortlisted, Interview Scheduled, Interview Completed, Offer Received, Accepted, Rejected, Withdrawn
- 📂 View applications filtered by status
- 🗃️ MySQL database with Django ORM — no raw SQL
- 🎨 Clean responsive UI with Bootstrap 5
- 🔐 Admin panel to manage all data
- 📅 Auto date tracking — date of application saved automatically

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Django |
| Database | MySQL |
| Frontend | HTML, CSS, Bootstrap 5 |
| ORM | Django ORM |
| Admin | Django Admin Panel |

---

## 📁 Project Structure

```
JobTracker/
│
├── myFirstProject/          # Django project config
│   ├── settings.py          # Database, installed apps, static files
│   ├── urls.py              # Main URL routing
│   └── __init__.py          # pymysql setup for MySQL connection
│
├── tracker/                 # Main app
│   ├── models.py            # JobApplication model
│   ├── views.py             # View functions
│   ├── urls.py              # App level URL routing
│   ├── admin.py             # Admin panel registration
│   ├── templates/
│   │   └── tracker/
│   │       ├── base.html            # Base template with navbar
│   │       ├── index.html           # Home page
│   │       ├── Applied.html         # Applied companies
│   │       ├── Rejected.html        # Rejected companies
│   │       ├── Pendding.html        # Pending companies
│   │       ├── about.html           # About page
│   │       └── contact.html         # Contact page
│   └── static/
│       └── tracker/
│           └── style.css            # Custom styles
│
├── manage.py                # Django management commands
└── requirements.txt         # Python dependencies
```

---

## 🗄️ Database Model

```python
class JobApplication(models.Model):
    company_name          # Name of the company
    role                  # Job role/position
    status                # Current application status (9 choices)
    office_location       # Office location
    salary                # Salary/CTC mentioned in JD
    date_of_application   # Auto saved when record created
    source_of_application # Where you found the job (LinkedIn, Naukri etc.)
    notes                 # Interview feedback, personal notes
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- MySQL
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/jobtracker.git
cd jobtracker
```

**2. Create and activate virtual environment**
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1    # Windows
source .venv/bin/activate      # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create MySQL database**
```sql
CREATE DATABASE job_tracker;
```

**5. Configure database in settings.py**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'job_tracker',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

**6. Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**7. Create superuser for admin panel**
```bash
python manage.py createsuperuser
```

**8. Run the server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` 🎉

---

## 📸 Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Landing page |
| Applied | `/Applied/` | All applied companies |
| Rejected | `/Rejected/` | All rejected companies |
| Pending | `/pending/` | All pending companies |
| About | `/about-us/` | About page |
| Contact | `/contact/` | Contact page |
| Admin | `/admin/` | Django admin panel |

---

## 📈 Project History

### Version 0.1 — April 2026
- ✅ Project setup with Django and MySQL
- ✅ JobApplication model with 9 status choices
- ✅ URL routing and function-based views
- ✅ Template inheritance with base.html
- ✅ Applied, Rejected, Pending pages with real MySQL data
- ✅ Bootstrap 5 navbar with working dropdown
- ✅ Admin panel configured

### Coming Soon
- 🔜 User authentication — login, register, logout
- 🔜 Add job form — submit applications from website
- 🔜 Dashboard with stats and charts
- 🔜 Edit and delete applications
- 🔜 Deploy to production

---

## 🤝 Contributing

This is a personal project built for placement purposes. Feel free to fork and build your own version.

---

## 📄 License

MIT License — free to use and modify.

---


