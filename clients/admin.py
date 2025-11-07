from django.contrib import admin
from .models import LeadSource, Lead, CallLog, Win

@admin.register(LeadSource)
class LeadSourceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class CallLogInline(admin.TabularInline):
    model = CallLog
    extra = 0

class WinInline(admin.TabularInline):
    model = Win
    extra = 0

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("business_name", "contact_name", "phone", "source", "owner")
    list_filter = ("source",)
    search_fields = ("business_name", "contact_name", "phone", "email")
    inlines = [CallLogInline, WinInline]

@admin.register(CallLog)
class CallLogAdmin(admin.ModelAdmin):
    list_display = ("lead", "who", "outcome", "when")
    date_hierarchy = "when"
    search_fields = ("lead__business_name", "who", "outcome")

@admin.register(Win)
class WinAdmin(admin.ModelAdmin):
    list_display = ("lead", "title", "when")
    date_hierarchy = "when"
