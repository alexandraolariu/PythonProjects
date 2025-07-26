from django.db import models

# Create your models here.

# core_api/models.py

from django.db import models
from django.utils import timezone

class ExtractionJob(models.Model):
    JOB_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    job_id = models.CharField(max_length=100, unique=True, db_index=True)
    status = models.CharField(max_length=20, choices=JOB_STATUS_CHOICES, default='pending')
    start_time = models.DateTimeField(auto_now_add=True)
    # Add other fields if strictly necessary for very basic representation

    class Meta:
        ordering = ['-start_time']

    def __str__(self):
        return f"Job {self.job_id} - {self.status}"

    def save(self, *args, **kwargs):
        if not self.job_id:
            self.job_id = f"job_{timezone.now().strftime('%Y%m%d%H%M%S%f')}"
        super().save(*args, **kwargs)