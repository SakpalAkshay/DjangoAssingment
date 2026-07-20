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

## Screeshots 
<img width="1091" height="677" alt="Screenshot 2026-07-20 142452" src="https://github.com/user-attachments/assets/418888d7-9398-40f4-80fd-2915c01a175c" />

<img width="1056" height="576" alt="Screenshot 2026-07-20 144907" src="https://github.com/user-attachments/assets/add05cc2-cc56-44aa-8b15-a0fe3e52d5a6" />

<img width="1087" height="431" alt="Screenshot 2026-07-20 144921" src="https://github.com/user-attachments/assets/909bf0de-80db-4a01-9629-557e02892428" />

<img width="1066" height="605" alt="Screenshot 2026-07-20 145022" src="https://github.com/user-attachments/assets/c8e22d8b-86e4-4b6b-9689-10140b5ee3d0" /> 

<img width="1087" height="851" alt="Screenshot 2026-07-20 145107" src="https://github.com/user-attachments/assets/a62bb1f8-4d52-4d5d-8f8d-4b13cea45624" />

<img width="1067" height="786" alt="Screenshot 2026-07-20 145213" src="https://github.com/user-attachments/assets/fc541314-302f-4dd8-a278-82d25d3018f4" />

<img width="1113" height="702" alt="Screenshot 2026-07-20 145535" src="https://github.com/user-attachments/assets/574ed907-125b-4635-8319-cad35b105ad3" />

<img width="1087" height="782" alt="Screenshot 2026-07-20 145600" src="https://github.com/user-attachments/assets/0474f2d7-5979-4073-8371-661f58a544d0" />

<img width="1095" height="683" alt="Screenshot 2026-07-20 145719" src="https://github.com/user-attachments/assets/f0e5b065-5963-470e-9b44-221df870a56d" />









