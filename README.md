# Mini Project 4 - Django Web App
**Author:** Janelle Holcomb  
**Class:** INF601 - Advanced Programming in Python (Mini Project 4)
---
## Project Overview

This Django app was built for my INF601 class. It includes authentication, forms, Bootstrap styling, and a SQLite database with connected models. I kept the layout clean and organized while focusing on clarity and purpose. 

The project, **Creative Systems Support**, is a simple business management tool that helps organize client information, track goals, log calls and wins, and outline services. It demonstrates Django’s full MVC structure and authentication system while keeping everything lightweight and easy to use.

### Pages
1.	**Home** (`/`) – overview of the app and quick navigation links
2.	**Clients** (`/leads/`) – list of all clients with a **Bootstrap modal** to add new clients
3.	**Client Detail** (`/leads/<id>/`) – edit client profiles, goals, and notes; log calls or wins
4.	**Wins** (`/wins/`) – displays all logged wins for each client
5.	**Scripts** (`/scripts/`) – placeholder page for outreach or communication templates
6.	**Services** (`/services/`) – lists the services and systems offered
7.	**Register** (`/register/`) – create a new user account
8.	**Login** (`/login/`) – log into an existing account
9.	**Logout** (`/logout/`) – securely log out and redirect to home
10.	**Admin** (`/admin/`) – manage all models in the Django admin panel
---
## Unique Touches
•	Renamed “Leads” to **Clients** to fit the real purpose of my project

•	Added **Bootstrap 5** styling and a working modal on the Clients page

•	Customized **Django Admin** with filters, search, and inlines

•	Prepared the structure to later include **goals, needs, and weekly tasks**

•	Used Django’s **built-in authentication** for register, login, and logout

•	Designed the layout to match my calm and organized brand style

---
## Requirements
Before running, make sure you have:

	Python **3.13+**

	`pip` (Python package manager)

	`venv` (for creating a virtual environment)

	Django **5.2.8**

---
## Installation and Setup
### 1. Create and activate a virtual environment
```bash
python -m venv .venv
```
## Windows
```bash
.venv\Scripts\Activate.ps1
```
## macOS/Linux
```bash
source .venv/bin/activate
```
### 2. Install all dependencies
```bash
pip install -r requirements.txt
```
This installs all required packages, including Django.

## Setting Up the Database
Run these commands in order to create and initialize the SQLite database:
```bash
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

```You can then log in to the admin panel at:

```cpp

http://127.0.0.1:8000/admin/
```
---
## Running the Django Development Server
```bash
python manage.py runserver
```
Then open your web browser and go to:
```cpp
http://127.0.0.1:8000/
```

You’ll be able to register, log in, view clients, and log wins.

## Tech Details
•	**Template Structure:** `base.html` defines the main layout with Bootstrap JS & CSS. All other templates extend this file.

•	**Forms:** Used for adding and editing clients. Form data is validated automatically through Django’s built-in form handling.

•	**Database:** SQLite database with models for `LeadSource`, `Lead`, `CallLog`, and `Win`, connected by foreign keys.

•	**Authentication:** Managed through Django’s built-in user authentication system.

•	**Bootstrap:** Used for responsive layouts, navigation, and a **modal** feature on the Clients page.

•	**Styling:** Clean layout with white space and soft color tones for a calm visual style.

---
## Updating Dependencies
If new packages are added later, update the requirements file:
```bash
pip freeze > requirements.txt
```
---
## Next Steps
•	**Add client login access** so each client can view their own goals and updates 

•	**Include progress tracking dashboards** for clients

•	**Add file uploads or shared notes** for collaboration

•	**Refine the home page design** to better reflect my brand and service focus

This version meets all the Mini Project 4 requirements and shows a working, organized Django web app with full authentication, forms, and Bootstrap integration.
## Instructor Header Reminder
Add this to the **top of every .py** file:
```python
# INF601 - Advanced Programming in Python
# Author: Janelle Holcomb
# Mini Project 4
```
