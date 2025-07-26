from django.contrib import admin

# Register your models here.
# core_api/admin.py

from django.contrib import admin
from .models import ExtractionJob

@admin.register(ExtractionJob)
class ExtractionJobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'status', 'start_time')
    list_filter = ('status',)
    search_fields = ('job_id',)
    readonly_fields = ('job_id', 'start_time',)