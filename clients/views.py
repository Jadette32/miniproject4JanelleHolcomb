# Author: Janelle Holcomb
# Class: INF 601 Mini Project 4
# Project: Creative Systems Support

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import Lead, CallLog, Win
from .forms import LeadForm, CallLogForm, WinForm, RegisterForm

def home(request):
    return render(request, "clients/home.html")

@login_required
def leads(request):
    my_leads = Lead.objects.filter(owner=request.user).order_by("business_name")
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.owner = request.user
            lead.save()
            messages.success(request, "Contact added.")
            return redirect("leads")
    else:
        form = LeadForm()
    return render(request, "clients/leads.html", {"leads": my_leads, "form": form})
@login_required
def services(request):
    return render(request, "clients/services.html")

@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk, owner=request.user)
    call_form = CallLogForm()
    win_form = WinForm()
    if request.method == "POST":
        if "add_call" in request.POST:
            call_form = CallLogForm(request.POST)
            if call_form.is_valid():
                c = call_form.save(commit=False)
                c.lead = lead
                c.save()
                messages.success(request, "Call logged.")
                return redirect("lead_detail", pk=pk)
        if "add_win" in request.POST:
            win_form = WinForm(request.POST)
            if win_form.is_valid():
                w = win_form.save(commit=False)
                w.lead = lead
                w.save()
                messages.success(request, "Win added.")
                return redirect("lead_detail", pk=pk)
    return render(request, "clients/lead_detail.html", {"lead": lead, "call_form": call_form, "win_form": win_form})

@login_required
def scripts(request):
    return render(request, "clients/scripts.html")

@login_required
def wins(request):
    my_wins = Win.objects.filter(lead__owner=request.user).order_by("-when")
    return render(request, "clients/wins.html", {"wins": my_wins})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome.")
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})
