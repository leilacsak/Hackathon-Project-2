# Hackathon Project 2

Tennis court booking starter built with Django, HTML templates, CSS, and Python.

## Current framework

Four pages are wired and ready for team development:

1. `/` - Home dashboard
2. `/courts/` - Court catalogue
3. `/book/` - Booking form
4. `/my-bookings/` - Booking list

## Project layout

- `booking_app/` - Django project settings and root URLs
- `core/models.py` - `Booking` model
- `core/forms.py` - `BookingForm`
- `core/views.py` - View logic for all 4 pages
- `core/templates/core/` - HTML templates
- `core/static/core/styles.css` - Shared CSS styling

## Run locally

```powershell
.\.venv\booking_app\Scripts\python.exe manage.py migrate
.\.venv\booking_app\Scripts\python.exe manage.py runserver
```

Then open `http://127.0.0.1:8000/`.
