<div align="center">

# 📕📙📒 헌책줄게 📒📙📕

## 👋 Intro 🤟

<b>헌책줄게</b>는  중고 책 거래 서비스입니다. 📚

👉 [더 알아보기](https://github.com/innovation-camp/heonchaegjulge/wiki) 👉

## 🎨 WireFrame 🖌

![Screen Shot 2022-08-04 at 12 25 36 PM](https://user-images.githubusercontent.com/60090391/182756494-25a64a89-af5d-46d5-8e68-ed7454e34847.png)

## 👩🏻‍💻 Contributors 🧑🏻‍💻

| [윤수진](https://github.com/blingblin-g) | [김정원](https://github.com/Dajeong09) | [박세은](https://github.com/marksenee) | [이다정](https://github.com/Dajeong09) | [장현욱](https://github.com/Artlogy) |
|---------------------------------------|---------------------------------|-------------------------------------|--------------------------|-----------------------------------|
| 로그인 / 로그아웃                            | 로그인 / 로그아웃                      | 게시글 CRUD                            | 게시글 CRUD                 | 게시글 목록<br/> / 웰컴페이지               |
|              Back-end                 |             Front-end                    |        Front-end                             |             Back-end             | Front-end                         |

## ⚙️ Tech Stack 🛠
<img style="margin:5px; border: 2px solid white; border-radius: 20px" src="https://img.shields.io/badge/Python-blue?style=flat-square&logo=python&logoColor=white"/>
<img style="margin:5px; border: 2px solid white; border-radius: 20px" src="https://img.shields.io/badge/Flask-gray?style=flat-square&logo=flask&logoColor=white"/>
<img style="margin:5px; border: 2px solid white; border-radius: 20px" src="https://img.shields.io/badge/MongoDB-darkgreen?style=flat-square&logo=mongodb&logoColor=white"/>
<img style="margin:5px; border: 2px solid white; border-radius: 20px" src="https://img.shields.io/badge/Jinja2-red?style=flat-square&logo=jinja&logoColor=white"/>
<img style="margin:5px; border: 2px solid white; border-radius: 20px" src="https://img.shields.io/badge/AWS-232f3e?style=flat-square&logo=amazon&logoColor=white"/>

</div>

## 🛼 How to run ⛸

### Python version
```shell
$ python -V
  Python 3.8.9
```

### clone repository
```shell
$ git clone https://github.com/innovation-camp/heonchaegjulge.git
```

### into the repository
```shell
$ cd heonchaegjulge
```

### install packages
```shell
$ pip install -r requirements.txt
```

### start app
```shell
$ flask run
```

## 📁 Directory Structure 📂

```shell
📦 app
 ┣ 📂 controller
 ┣ 📂 decorators
 ┣ 📂 middleware
 ┣ 📂 static
 ┃ ┣ 📂 css
 ┃ ┣ 📂 image
 ┃ ┣ 📂 js
 ┣ 📂 templates
 ┃ ┣ 📂 account
 ┃ ┣ 📂 components
 ┃ ┣ 📂 error
 ┃ ┣ 📂 post
 ┣ 📜 __init__.py
 ┣ 📜 constants.py
 ┣ 📜 db.py
 ┗ 📜 utils.py
```

## 💾 Database Schema 💿

### User

```python
    {
        _id: <ObjectId>,
        nickname: "haha",
        email: "abc@gmail.com",
        password: "sljriowqejfj3weo;'qfijewoj124j!" # hashing
        created_at: DATETIME
    }
```

### Post

```python
{
	_id: <ObjectId>
	title:
	description:
	created_at:
	updated_at:
	is_selling:
	condition:
	price:
	writer: {
                    id: , 
                    nickname:
                }
	is_soldout:
	location:
	genre:
	contact:
}
```
