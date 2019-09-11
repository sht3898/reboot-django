from django.shortcuts import render, redirect
from .models import Job
from faker import Faker

# Create your views here.
def index(request):
    jobs = Job.objects.order_by('-pk')
    context = {
        'jobs' : jobs
    }
    return render(request, 'jobs/index.html', context)

def find(request):
    name = request.POST.get('name')
    job = Job.objects.filter(name=name)
    if not job:
        fake = Faker('ko_KR')
        job = fake.job()
        job = Job.objects.create(name=name, job=job)
    else:
        job = job[0]
    context = {
        'job' : job
    }
    return render(request, 'jobs/find.html', context)
