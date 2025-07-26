# core_api/urls.py

from django.urls import path
from .views import (
    HealthCheckView,
    ListJobsView,
    CreateJobView
)


print(f"Type of CreateJobView in urls.py: {type(CreateJobView)}")

urlpatterns = [
    path('health', HealthCheckView.as_view(), name='health_check'),
    path('jobs', ListJobsView.as_view(), name='list_jobs'),
    path('jobs/create', CreateJobView.as_view(), name='create_job'),
]