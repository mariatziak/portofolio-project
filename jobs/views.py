from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects # to get all the jobs from the db
    return render(request, 'jobs/home.html', {'jobs': jobs})
