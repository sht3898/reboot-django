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

