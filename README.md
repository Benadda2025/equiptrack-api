# equiptrack-api

Backend API for EquipTrack: manage equipment, categories, bookings, and maintenance records with JWT auth and role-based access.

Built with [Flask AppBuilder](https://flask-appbuilder.readthedocs.io/) (FAB) and PostgreSQL.

## 1. Start the dev container

Requirements: Docker and VS Code with the **Dev Containers** extension.

1. Open the repo root (`equiptrack-api`) in VS Code.
2. `Ctrl+Shift+P` → **Dev Containers: Reopen in Container**.
3. Wait for the first build to finish, then open a new terminal and check:

```bash
pwd              # /workspaces/equiptrack-api
flask --version  # Flask and Flask-AppBuilder versions
```

The container gives you Python 3.12 and a Postgres 16 service reachable at host `db`
(user / password / database: `equiptrack`). Connection settings are provided through
the `SQLALCHEMY_DATABASE_URI`, `SECRET_KEY` and `JWT_SECRET_KEY` environment variables.

## 2. Create the app

From the repo root, inside the container:

```bash
flask fab create-app --name equiptrack --engine SQLAlchemy
```

This downloads the FAB skeleton from GitHub (internet access required) and creates:

```
equiptrack/
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── views.py
├── config.py
└── run.py
```

Move into the new folder. All following commands run from here:

```bash
cd equiptrack
```

`FLASK_APP=app` is already set in the container, so `flask` commands work in this folder.

### Use Postgres instead of SQLite

The skeleton defaults to SQLite. Open `equiptrack/config.py` and replace the database
and secret settings with:

```python
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI",
    "sqlite:///" + os.path.join(basedir, "app.db"),
)
```

Inside the container the environment variable points at the `db` service, so the app uses Postgres automatically.

## 3. Create the admin user

```bash
flask fab create-admin
```

You will be prompted for username, first name, last name, email and password.
The `Admin` role is assigned automatically.

If the command fails because tables are missing, initialise the database first:

```bash
flask fab create-db
flask fab create-admin
```

Other useful user commands:

```bash
flask fab list-users
flask fab create-user --role Admin    # add another user
flask fab reset-password --username admin
```

## 4. Run the app

```bash
flask run --host 0.0.0.0
```

VS Code forwards port 5000. Open <http://localhost:5000> and log in with the admin
account you just created.

## 5. Test JWT auth

FAB exposes a login endpoint that returns a JWT:

```bash
curl -X POST http://localhost:5000/api/v1/security/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "YOUR_PASSWORD", "provider": "db", "refresh": true}'
```

Use the returned `access_token` on API calls:

```bash
curl http://localhost:5000/api/v1/<your_resource>/ \
  -H "Authorization: Bearer <access_token>"
```

## Next steps

- Add models (equipment, categories, bookings, maintenance) in `app/models.py`.
- Expose them as REST endpoints with `ModelRestApi` and register them in `app/__init__.py`.
- Create roles and permissions from the web UI under **Security**.