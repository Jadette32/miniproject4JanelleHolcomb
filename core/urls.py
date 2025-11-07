# INF601 - Advanced Programming in Python
# Author: Janelle Holcomb
# Mini Project 4

from django.contrib import admin
from django.urls import path
from clients import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", v.register, name="register"),
    path("", v.home, name="home"),
    path("leads/", v.leads, name="leads"),
    path("leads/<int:pk>/", v.lead_detail, name="lead_detail"),
    path("scripts/", v.scripts, name="scripts"),
    path("wins/", v.wins, name="wins"),
    path("services/", v.services, name="services"),

]
