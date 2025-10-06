# Polls App

![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-5.2.7-green)
![AWS Elastic Beanstalk](https://img.shields.io/badge/AWS-Elastic%20Beanstalk-orange)

---

## Project Overview
The **Polls App** is a simple Django application that allows users to view polls and their choices.  
It is deployed on **AWS Elastic Beanstalk** with **SQLite** as the backend database.

**Deployed URL:**  
[Polls App Live](http://polls-se-env.eba-2vxmtbk5.us-west-2.elasticbeanstalk.com/polls/)

---

## Features
- View a list of polls  
- View poll details and available choices  
- Seed sample polls and choices for testing  
- Deployed to the cloud for easy access  

---

## Local Setup

1. **Create and activate a virtual environment**
```bash
python3 -m venv myenv
source myenv/bin/activate
---
2. **Install dependencies**
```bash
pip install -r requirements.txt

3. **Run migrations and start the server**

python manage.py migrate
python manage.py runserver

4. **Access locally**

http://127.0.0.1:8000/polls/

## AWS Elastic Beanstalk Deployment

1. **Install EB CLI and configure your AWS account.**

Create .ebextensions/django.config with:

option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: "SEassignment1.settings"
    PYTHONPATH: "/var/app/current:$PYTHONPATH"
  aws:elasticbeanstalk:container:python:
    WSGIPath: SEassignment1.wsgi:application


2. **Initialize EB CLI and create an environment:**

eb init
eb create polls-env
eb deploy


3. **Configure persistent SQLite database in settings.py:**

import os
SQLITE_PATH = os.environ.get("SQLITE_PATH", str(BASE_DIR / "db.sqlite3"))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": SQLITE_PATH,
    }
}


4. **SSH into the instance and run migrations as webapp user:**

eb ssh
sudo mkdir -p /var/app/data
sudo chown -R webapp:webapp /var/app/data
sudo chmod 775 /var/app/data
sudo -u webapp -H bash -lc '
  source /var/app/venv/*/bin/activate
  cd /var/app/current
  python manage.py migrate --noinput
'

