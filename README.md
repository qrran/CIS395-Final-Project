# Student Support Database System

The key idea here is we are able get a comprehensive understanding from the data in community engagement table of which group of students are active, hence provide support to student groups who are inactive by creating relevant workshops or activities to stimulate student engagement from diverse cultural background.

## 1. About

Student Support Database System includes two interactive databases:

- [Tables](./student_support_system/webapp/models.py)

1. [Student Information Table](./img/student_information.png)

- contains student information

2. [Community Engagement Table](./img/community_engagement.png)

- stores data about students' community engagement, indicates students' activities outside of classes

Notes: the insert/update/delete button for Community Engagement Tables are needed to optimize

## 2. Tech Stack

- Frontend:

  - HTML/CSS
  - Libraries: Bootstrap CSS, Code Pen CSS

- Backend:

  - Python
  - SQLite

- Framework:
  - Django

## 3. Run the Project

1. virtual environment:<br>
   `python3 -m venv .env`<br>
   `source .venv/bin.activate`<br>
   `pip3 install -r requirements.txt`

2. Go to the project directory: <br>
   `cd student_support_system`

3. run the server:<br>
   `python3 manage.py runserver`<br>
   note: python version may differ, here used python3.10

4. /admin

- username: `ld`
- password: `Djangoapp1`
