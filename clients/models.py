# Author: Janelle Holcomb
# Class: INF 601 Mini Project 4
# Project: Creative Systems Support

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class LeadSource(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Lead(models.Model):
    business_name = models.CharField(max_length=150)
    contact_name = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    source = models.ForeignKey(LeadSource, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="css_leads")
    def __str__(self):
        return self.business_name

class CallLog(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="calls")
    when = models.DateTimeField(auto_now_add=True)
    who = models.CharField(max_length=120, blank=True)
    outcome = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    def __str__(self):
        return f"{self.lead} — {self.outcome} @ {self.when:%Y-%m-%d %H:%M}"

class Win(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="wins")
    title = models.CharField(max_length=150)
    when = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} — {self.lead}"
