# core_api/views.py
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import ExtractionJob # Assuming this model still exists and is correct
from django.forms.models import model_to_dict

class HealthCheckView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'status': 'ok'})

class ListJobsView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'ListJobsView is working, implement your logic here.'})


@csrf_exempt
class CreateJobView(View):

    def post(self, request, *args, **kwargs):
        return JsonResponse({'message': 'CreateJobView is working, implement your POST logic here.'})

