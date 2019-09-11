# REBOOT Django

## 프로젝트 및 앱 생성

```bash
$ python -m venv venv
$ source venv/Scripts/activate	# vi로 파일만들어서 activate로 생략
$ pip install django
$ django-admin startproject reboot . # 뒤에 점 중요
$ python manage.py startapp articles
```

* `bashrc` 작성 - 단축키로 사용 가능

  ```bash
  $ vi ~/. bashrc
  ```

  ```txt
  alias jn='jupyter notebook'
  alias venv="source ~/python-virtualenv/3.7.4/Scripts/activate"
  venv
  alias activate="source venv/Scripts/activate"
  ```

* gitignore 등록

  ```bash
  $ vi .gitignore
  ```

  ```txt
  venv/
  .vscode/
  __pycache__/
  ```




## setting.py 정보 설정

### INSTALLED_APPS에 articles 앱 추가

```python
# reboot/settings.py
...
INSTALLED_APPS = [
    'articles',		# 생성한 articles 앱 추가
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
...
```

### 언어 및 시간 설정

```python
# reboot/settings.py
...
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
...
```



## Article 모델 생성

```python
# articles/models.py

from django.db import models

# Create your models here.
# 1. 모델(스키마) 정의
# 데이터베이스 테이블을 정의하고,
# 각각의 컬럼(필드) 정의
class Article(models.Model):
    # id : integer 자동으로 정의(Primary Key)
    # id = models.AutoField(primary_key=True) -> Integer 값이 자동으로 하나씩 증가(AUTOINCREMENT)
    # CharField - 필수인자로 max_length 지정
    title = models.CharField(max_length=10)
    content = models.TextField()
    # DateTimeField
    #    auto_now_add : 생성시 자동으로 저장
    #    auto_now : 수정시마다 자동으로 저장
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} : {self.title}'

# models.py : python 클래스 정의
#           : 모델 설계도
# makemigrations : migration 파일 생성
#           : DB 설계도 작성
# migrate : migration 파일 DB 반영
```





## url 설정

### reboot url 설정

```python
# reboot/urls.py

from django.contrib import admin
from django.urls import path, include	# include 추가
# from articles import views	# articles의 views 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]	# articles의 urls을 포함하면 저절로 articles/ 주소 부여
```



### articles url 설정

* articles 폴더에 urls.py 생성

* articles/urls.py

  ```python
  from django.urls import path
  from . import views	# 현재 디렉토리(.)에서 views를 import
  
  app_name = 'articles'	# app 이름을 통해 접근할 수 있게 함
  
  urlpatterns = [
      path('', views.index, name='index'),
  ]
  ```



## base html 생성

* articles 폴더에 templates 폴더를 생성하고, templates 폴더 안에 articles 폴더 생성

* 나머지 html의 기본이 될 base.html 생성 - Bootstrap 포함

* articles/templates/aritcles/base.html

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
      {% block css %}{% endblock  %}
  </head>
  <body>
      {% block body %}
      {% endblock  %}
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
  </html>
  ```



## 기본 화면(index) 생성

### url 추가

```python
# articles/urls.py
...
urlpatterns = [
    path('', views.index, name='index'),
]
```



### views.py 추가

* Article 모델 정보 가져오기

  ```python
  # articles/views.py
  from django.shortcuts import render
  from .models import Article	# 현재 디렉토리에 있는 models(.models)에서 가져옴
  ```

* def index 작성

  ```python
  # articles/views.py
  def index(request):
      articles = Article.objects.order_by('-id')	# 내림차순 정렬
      context = {
          'articels' : articles
      }
      return render(request, 'articles/index.html', context)
  ```



### index.html 생성

* articles/templates/articles에 생성

* index.html

  ```html
  {% extends 'articles/base.html' %}
  {% block css %}
  <style>
    tr > th:nth-of-type(2) {
      width: 50%;
    }
  </style>
  {% endblock %}
  {% block body %}
    <h1 class="text-center">게시판에 오신걸 환영합니다.</h1>
    <table class="table mt-5">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">제목</th>
          <th scope="col">작성일자</th>
        </tr>
      </thead>
      <tbody>
        {% for article in articles %}
        <tr>
          <th scope="row">{{ article.id }}</th>
          <td>
            <a href="{% url 'articles:detail' article.pk %}">
                {{ article.title }} <!-- detail로 연결 -->
            </a>
          </td>
          <td>{{ article.created_at }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  {% endblock %}
  ```

  

## migrate

> Django에서 Model 클래스를 생성하고 난 후, 해당 모델에 상응하는 테이블을 데이타베이스에서 생성할 수 있다. Python 모델 클래스의 수정 (및 생성 )을 DB에 적용하는 과정을 Migration이라 부른다. 이는 Django가 기본적으로 제공하는 ORM (Object-Relational Mapping) 서비스를 통해 진행된다.

### makemigrations - 마이그레이션 파일 생성

```bash
$ python manage.py makemigrations
```

### migrate - 마이그레이션 파일 DB에 반영

```bash
$ python manage.py migrate
```



## 실행해서 확인

```bash
$ python manage.py runserver
```



## 영화 세부 정보(detail) 생성

### url 추가

```python

```

