# DjangoProject — Django Login System

A Django project implementing user **signup, login, and profile management** with full **CRUD** operations, built for the ConsultAdd Django training assignment.

The project uses Django's built-in features for model creation, views, URL routing, and template rendering, and exposes JSON endpoints that can be tested with Postman.

---

## Project structure

```
DjangoProject/
├── manage.py
├── requirements.txt
├── README.md
├── login_system/            # Django project (settings, root URLs)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
└── Loginify/                # Django app handling login functionality
    ├── models.py            # UserDetails model
    ├── views.py             # hello_world, signup, login + CRUD views
    ├── urls.py              # app URL patterns
    ├── admin.py             # UserDetails registered in admin
    ├── migrations/
    └── templates/Loginify/
        ├── base.html
        ├── signup.html
        ├── login.html
        └── success.html
```

- **Project name:** `login_system` (assignment: "Login System")
- **App name:** `Loginify`
- **Virtual environment:** `DjangoAssignment`

---

## The model — `UserDetails`

| Field    | Definition                                       |
|----------|--------------------------------------------------|
| username | `CharField(max_length=50, primary_key=True)`     |
| email    | `EmailField(unique=True)`                         |
| password | `CharField(max_length=12, blank=True)`            |

---

## Setup & run

1. **Create and activate the virtual environment**
   ```bash
   python3 -m venv DjangoAssignment
   source DjangoAssignment/bin/activate      # Windows: DjangoAssignment\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser** (Task 4)
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/`.

---

## Endpoints

### Pages & auth (HTML templates)

| Method | URL          | Description                                                        |
|--------|--------------|-------------------------------------------------------------------|
| GET    | `/hello/`    | Returns plain text `Hello, world!` (Task 2 test view)             |
| GET    | `/signup/`   | Renders the signup form                                            |
| POST   | `/signup/`   | Registers a user; on success **redirects to `/login/`**           |
| GET    | `/login/`    | Renders the login form                                            |
| POST   | `/login/`    | Authenticates by email + password; on success shows success page  |

### CRUD API (JSON — test with Postman) (Task 5)

| Method | URL                              | Description                              |
|--------|----------------------------------|------------------------------------------|
| GET    | `/users/`                        | **Read all** — list every user           |
| GET    | `/users/<email>/`                | **Read one** — get a user by email        |
| PUT    | `/users/<email>/update/`         | **Update** — change email and/or password |
| DELETE | `/users/<email>/delete/`         | **Delete** — remove a user by email       |

The `signup` and `login` views accept **both** HTML form posts (from the templates) and raw JSON bodies (from Postman). Send JSON with header `Content-Type: application/json`.

---

## Testing with Postman

**Create a user (JSON signup)**
```
POST http://127.0.0.1:8000/signup/
Content-Type: application/json

{ "username": "alice", "email": "alice@example.com", "password": "alicepw" }
```

**Read all users**
```
GET http://127.0.0.1:8000/users/
```

**Update a user**
```
PUT http://127.0.0.1:8000/users/alice@example.com/update/
Content-Type: application/json

{ "password": "newpw123", "email": "alice.new@example.com" }
```

**Delete a user**
```
DELETE http://127.0.0.1:8000/users/alice.new@example.com/delete/
```

---

## Notes

- Passwords are stored as plain text per the assignment's model spec (`max_length=12`). This is for learning purposes only and is **not** suitable for production — use Django's `auth` system and password hashing for real applications.
- `csrf_exempt` is applied to the auth/CRUD views so they can be exercised directly from Postman. In a browser-only app you would keep CSRF protection enabled and rely on the `{% csrf_token %}` already present in the templates.

---

## Screenshots

_Add screenshots of the rendered templates and Postman responses here (assignment instruction 3)._
