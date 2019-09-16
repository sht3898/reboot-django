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



# Reporter, Comment 모델 생성

## 모델 생성

```python
# Create your models here.
# Reporter(1) - Article(N)
# reporter - name
class Reporter(models.Model):
    name = models.CharField(max_length=30)


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)


# Article(1) - Comment(N)
# comment - content
class Comment(models.Model):
    comment = models.CharField(max_length=30)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```



## migrate

```bash
$ python manage.py makemigrations

$ python manage.py migrate
```

여기서 오류 발생하면 migrations, db.sqlite3 파일 제거



## Shell_Plus 실행

```bash
$ pip install django_extensions
# settings.py에서 app에 django_extensions 추가
$ python manage.py shell_plus
```



## reporter 생성

```bash
In [1]: reporter1 = Reporter()

In [2]: reporter1.name = '홍길동'

In [3]: reporter1.save()

In [4]: reporter2 = Reporter.objects.create(name='철수')
```

In[1]~[3]과 In[4]는 같은 방법



## 오브젝트를 통한 방법

```bash
article.title = '1번글'

article.content = '1번 내용'

article.reporter = reporter1
# reporter1을 저장하지 않으면 constraint 오류
article.save()
```



## article_set을 통해서

```shell
In [19]: article2 = Article.objects.create(title='제목', content='내용', reporter=1)
# 이렇게 reporter에 1을 저장하면 오류 발생 => 1이 아닌 Reporter 인자를 써야함

In [20]: article2 = Article.objects.create(title='제목', content='내용', reporter_id=1)
# 이렇게 reporter가 아닌 reporter_id로 쓰면 가능

In [21]: article3 = Article.objects.create(title='제목', content='내용', reporter=reporter1)

In [22]: article4 = Article()

In [23]: article4.title = '제목'

In [24]: article4.content = '내용'

In [25]: article.reporter_id = 1

In [26]: article.save()
```



## 쿼리 조회

```shell
In [27]: reporter2.article_set.all()
Out[27]: <QuerySet []>

In [28]: reporter1.article_set.all()
Out[28]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>

In [29]: Article.objects.filter(reporter_id=1)
Out[29]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>

```

In[28]과 In[29]는 동일한 결과



```shell
In [30]: article3
Out[30]: <Article: Article object (3)>

In [31]: article3.reporter
Out[31]: <Reporter: Reporter object (1)>

In [32]: article3.reporter_id
Out[32]: 1
```






```shell
In [33]: article4.reporter = reporter2

In [34]: article4.save()

In [35]: article4.reporter
Out[35]: <Reporter: Reporter object (2)>

In [36]: reporter1.article_set.add(article4)

In [37]: article4.reporter
Out[37]: <Reporter: Reporter object (1)>
```





## article1에 댓글 두개 추가

```shell
article1.
```





## 마지막 댓글의 기사를 작성한 기자

```shell
In [62]: comment2.article.reporter
Out[62]: <Reporter: Reporter object (1)>

In [63]: comment2.article.reporter.name
Out[63]: '서현택'
```



## 기사별 댓글 내용 출력

```shell
In [64]: articles = Article.objects.all()

In [65]: articles
Out[65]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>, <Article: Article object (4)>]>

In [66]: for article in articles:
    ...:     for comment in article.comment_set_all():
    ...:         print(comment.content)
    
댓글2
댓글1
```



## 기자별 기사 내용 출력

```shell
In [82]: reporters = Reporter.objects.all()

In [83]: reporters
Out[83]: <QuerySet [<Reporter: Reporter object (1)>, <Reporter: Reporter object (2)>]>

In [84]: for reporter in reporters:
    ...:     print(reporter.name)
    ...:     for article in reporter.article_set.all():
    ...:         print(article.title)
```



## reporter1의 기사 갯수

```shell
In [85]: reporter1.article_set.count()
Out[85]: 4
```

