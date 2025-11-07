# Creative Systems Support


Creative Systems Support is a simple business management web app built with Django for Mini Project 4.
It’s designed to help organize client relationships, goals, and weekly progress in one place.

The site lets me:

Create and manage client profiles with goals, needs, and notes

Log calls and wins for each client

Store outreach and communication templates

Outline available services and support options

Use a secure login system to protect client information

This project reflects the kind of work I do, helping small business owners bring structure and calm to their workflow.
Right now, it functions as my personal hub for managing clients and systems.
Later, it could grow into a shared platform where clients can view their own progress or updates.
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

## Pages
- Home page at `/`
- Clients page at `/leads/` with a pop up form
- Client detail page at `/leads/<id>/` to edit the profile and log calls and wins
- Templates page at `/scripts/`
- Wins page at `/wins/`
- Register at `/register/`, Login at `/login/`, Logout at `/logout/`
- Admin at `/admin/`
- Services at `/services/` 


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
