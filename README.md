

# 📌 Social Media API

A simple **social media REST API** built with **Django REST Framework** and **JWT authentication**.
Users can register, login, create posts, and add comments.

---

## 🚀 Features

* User registration & JWT authentication (login/refresh)
* Create, read, update, delete (CRUD) posts
* Add comments to posts
* Authenticated actions (posts/comments require login)

---

## 🛠️ Tech Stack

* **Django** & **Django REST Framework (DRF)**
* **JWT Authentication** via `djangorestframework-simplejwt`
* **SQLite** (default, can be swapped for PostgreSQL/MySQL)

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/your-username/socialapi.git
cd socialapi

# Create virtual environment
python -m venv venv
source venv/bin/activate   # on macOS/Linux
venv\Scripts\activate      # on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser (optional, for admin panel)
python manage.py createsuperuser

# Run server
python manage.py runserver
```

---

## 🔑 Authentication Endpoints

| Method | Endpoint              | Description                |
| ------ | --------------------- | -------------------------- |
| POST   | `/api/auth/register/` | Register a new user        |
| POST   | `/api/auth/login/`    | Login, returns JWT tokens  |
| POST   | `/api/auth/refresh/`  | Refresh JWT token          |
| GET    | `/api/auth/me/`       | Get current logged-in user |

### Example Login Response

```json
{
  "refresh": "your-refresh-token",
  "access": "your-access-token"
}
```

Use the **access token** in headers:

```
Authorization: Bearer your-access-token
```

---

## 📝 Posts API

| Method | Endpoint           | Description                       |
| ------ | ------------------ | --------------------------------- |
| GET    | `/api/posts/`      | List all posts                    |
| POST   | `/api/posts/`      | Create a new post (auth required) |
| GET    | `/api/posts/<id>/` | Retrieve a single post            |
| PUT    | `/api/posts/<id>/` | Update a post (author only)       |
| DELETE | `/api/posts/<id>/` | Delete a post (author only)       |

**Example Request:**

```http
POST /api/posts/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "title": "My First Post",
  "content": "This is the content of my first post."
}
```

---

## 💬 Comments API

| Method | Endpoint                         | Description                    |
| ------ | -------------------------------- | ------------------------------ |
| GET    | `/api/posts/<post_id>/comments/` | List comments for a post       |
| POST   | `/api/posts/<post_id>/comments/` | Add a comment (auth required)  |
| GET    | `/api/posts/comments/<id>/`      | Retrieve a single comment      |
| PUT    | `/api/posts/comments/<id>/`      | Update a comment (author only) |
| DELETE | `/api/posts/comments/<id>/`      | Delete a comment (author only) |

**Example Request:**

```http
POST /api/posts/1/comments/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "content": "Nice post!"
}
```

---

## 📂 Project Structure

```
socialapi/
├── accounts/       # User registration & authentication
├── posts/          # Post & comment models, views, serializers
├── socialapi/      # Project settings & root URLs
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 🖥️ Testing

You can test endpoints with:

* [Postman](https://www.postman.com/)
* [HTTPie](https://httpie.io/)
* cURL in the terminal

---

## 📜 License

MIT License – free to use & modify.

---
Best Regards, Ali Sena Danishwer
