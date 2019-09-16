# 전생 app

무연님은 전생에 선생님이었습니다.

1. Model 정의

1. Form : 이름을 받아서

2. 직업 랜덤 추출

   ```python
   fake.job()
   ```

3. 결과를 출력

   1. DB에 등록된 이름이 있으면, 해당하는 결과를
   2. 이름이 없으면 새롭게 DB에 추가하고, 결과 출력



* faker 설치

  ```bash
  $ pip install faker
  ```

  ```bash
  $ python -i
  Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  >>> from faker import Faker
  >>> fake = Faker()
  >>> fake.name()
  'Jeffrey Mcgee'
  >>> fake.address()
  '392 Andrade Neck Suite 873\nJessicafurt, NY 93642'
  >>> fake.text()
  'Us true include. Choose natural no candidate. Break site customer customer dog. Cold whole laugh single.\nEarly movement near hold bit push expect. Never feel tree our final situation state.'
  ```

  

* 모델명을 바꿨다면 저장소를 지우고 마이그레이션 작업을 다시 해야함

* urls.py에 APP_NAME 을 적지 않으면 jobs:result 같은 것을 입력했을 때 오류 발생

* GET을 쓰면 안되는 이유 - 빈 리스트에서 오류 발생

* Filter를 써야하는 이유 - 빈 리스트에서 오류 발생 x

  ex) 

  ```bash
  PastLife.objects.filter(name=name)
  ```

```python
def result(request):
    name = request.GET.get('name')
    past_life = PastLife.objects.filter(name=name)[0]
    # DB에 이름이 있으면,
    if not past_life:
        # 이름이 없으면
        fake = Faker('ko_KR')
        job = fake.job()
        past_lift = PastLife.objects.create(name=name, job=job)
        context = {
            'past_life' : past_life
        }
        return render(request, 'jobs/result.html', context)
```





# giphy api

## api 값 숨기기

```bash
$ pip install python-decouple
```

```txt
# reboot-django2/.env

GIPHY_API_KEY = '~~~~~'
```

```python
from decouple import config
api_key = config('GIPHY_API_KEY')
```

```txt
# .gitignore 파일에도 추가
.env
```





# 카카오 형태소부

