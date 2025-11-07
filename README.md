# Creative Systems Support

Creative Systems Support is a small Django web app I built for Mini Project 4. It is a simple system that keeps track of contacts, call notes, and wins for any kind of business or outreach work.

## Setup

Open a terminal in the project folder and run:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\Activate.ps1
# Mac or Linux
source .venv/bin/activate
pip install -r requirements.txt
```

If you ever need to update the list of packages, run:

```bash
pip freeze > requirements.txt
```

## Setting up the database

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Running the server

```bash
python manage.py runserver
```

Then open http://127.0.0.1:8000/

## Pages

- Home page at `/`
- Contacts page at `/leads/` with a pop up form
- Contact detail page at `/leads/<id>/` to log calls and wins
- Scripts page at `/scripts/`
- Wins page at `/wins/`
- Register at `/register/`, Login at `/login/`, Logout at `/logout/`
- Admin at `/admin/`

## Project structure

```
core/       project settings and urls
clients/    app code for models, forms, views, and admin
templates/  html templates including base and page templates
static/     any custom style files or images
requirements.txt
README.md
manage.py
```

## Common commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
