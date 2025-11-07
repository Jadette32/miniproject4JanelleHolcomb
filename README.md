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

## Where each project requirement is met

- Initial comments
Every major Python file includes my name, class, and project information at the top.

- Proper imports
Each file only imports what it uses, including models, views, and admin.

- Folder structure
The project includes one app called clients and follows the correct Django layout with core, templates, and static folders.

- Five pages with templates
The project includes a home page, clients page, client detail page, templates page, and wins page.
A services page is also included as an additional section.

- At least one page with a form
The clients page has a Bootstrap modal that lets me add a new client.
The client detail page also includes forms to update goals, needs, and tasks.

- Django admin setup
All models are registered and styled for easy entry with filters, search fields, and inline options.

- Bootstrap usage
Bootstrap 5 is used in the base layout for clean styling.
The clients page includes a modal, which fulfills the Bootstrap requirement.

- Register and login system
The register, login, and logout pages are fully functional.
Logout uses a secure POST method from the navbar.
Redirects are set up in core/settings.py with
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
LOGIN_URL = "login"

- Five commits minimum
The project includes multiple meaningful commits showing the build process step by step.

- requirements.txt
The file lists all required packages and can be updated with pip freeze.

- README completeness
This file includes every setup step, Django command, and explanation required by the Mini Project 4 rubric.

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
## Notes

Bootstrap 5 is active on the clients page with a working modal.
The login system redirects correctly for protected pages.
Admin shows all models with lists, filters, and inline sections.
This README includes every command required by the rubric.