# git

git 명령어 입력하기 전에 상위 디렉토리에 git 폴더가 있는지 확인해서 있다면 하나만 남겨야 함



wq : write + quit

```bash
$ git log	# git 기록

$ git config --global user.email	# user email 등록

$ git config --global --list	# 등록된 user email 확인

$ git remote add origin		# 새로운 git 저장소 연결

$ git remote -v		# 현재 등록된 저장소 확인
					# clone으로 끌어오면 그 저장소가 origin이 되기 때문에 gitlab과 github를 같이 사용할 때는 주의해서 사용
					
$ git reset HEAD <file> to unstage

$ git reset HEAD b.txt		# b.txt를 git add에서 제거할 수 있음

$ git commit -m 'a.txt 수정'

$ git log --oneline		# git log를 한 줄로 깔끔하게 보기

$ git commit --amend		# git commit 했던 것을 수정할 수 있음
```



commit 이후에 새로운 데이터를 추가하고 싶으면

```bash
$ git add a.txt

$ git commit -m 'a.txt 저장'	# a.txt만 commit 되어있는 상태

$ git add b.txt

$ git commit --amend		# 현재 무대 위에 있는 것을 모두 올림
```



이전 commit으로 돌아가는 것

```bash
$ git checkout -- a.txt
```



working directory에서 빼줄 수 있음

```bash
$ git rm --cached -r __pycache__
```



모든 csv 확장자 무시하기

```bash
*.csv
*/__pycache__/*
```



commit 할 때 지금 있는 변화를 모두 저장시켜라

```bash
$ git commit -am 'Edit gitignore'
```



git 상태 돌리기

```bash
$ git log --oneline	# 앞에 나오는 번호 확인
$ git reset --hard 번호
```

git reset과 git revert 의 차이?

git revert는 기록을 남김

git reset