# DjangoProject

This is my Django assignment project. It's a simple login system where users can sign up, log in, and I also added CRUD API endpoints that I tested with Postman.

App name is `Loginify`, project name is `login_system`.

## Model

UserDetails has:
- username (primary key)
- email (unique)
- password (plain text, max 12 chars - just for this assignment)

## How to run it

```
python -m venv DjangoAssignment
DjangoAssignment\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then go to http://127.0.0.1:8000/

## Pages

- `/hello/` - just returns "Hello, world!" (test view)
- `/signup/` - signup form
- `/login/` - login form, redirects to a success page

## CRUD API (tested in Postman)

- GET `/users/` - all users
- GET `/users/<email>/` - one user
- PUT `/users/<email>/update/` - update email/password
- DELETE `/users/<email>/delete/` - delete user

Signup/login views accept normal form posts and also JSON (for Postman), just set the Content-Type header to application/json.

## Notes

- Passwords are stored as plain text right now, I know that's bad practice but it's what the assignment model asks for. Would use Django's auth system + hashing for a real app.
- CSRF is turned off on these views so Postman can hit them directly.
