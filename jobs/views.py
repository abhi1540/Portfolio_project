from django.shortcuts import render
from django.conf import settings
from .models import Job
# Create your views here.


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'MEDIA_URL': settings.MEDIA_URL, 'jobs': jobs})

