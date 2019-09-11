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
    past_life = Job.objects.filter(name=name).first()
    if not past_life:
        # fake = Faker('ko_KR')
        fake = Faker('en_US')
        job = fake.job()
        past_life = Job.objects.create(name=name, job=job)
    # 직업 결과에 따라, giphy 요청
    job = past_life.job
    from decouple import config
    api_key = config('GIPHY_API_KEY')
    # 1. url 설정
    # url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={job}&lang=ko'
    url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={job}&lang=en'
    
    import requests
    # 2. 요청 보내기
    response = requests.get(url).json()
    # 3. 응답 결과에서 이미지 url 뽑기
    print(response)
    try:
        image_url = response['data'][0].get('images').get('original').get('url')
    except:
        image_url = None
    context = {
        'job' : past_life,
        'image_url' : image_url
    }

    return render(request, 'jobs/find.html', context)
