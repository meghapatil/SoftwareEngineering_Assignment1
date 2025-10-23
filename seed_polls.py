# seed_polls.py
import os, django
os.environ["SQLITE_PATH"] = "/var/app/data/db.sqlite3"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SEassignment1.settings")
django.setup()
from polls.models import Question, Choice
from django.utils import timezone

q1, _ = Question.objects.get_or_create(
    question_text="Which framework do you like most?",
    defaults={"pub_date": timezone.now()}
)
Choice.objects.get_or_create(question=q1, choice_text="Django", defaults={"votes": 0})
Choice.objects.get_or_create(question=q1, choice_text="Flask", defaults={"votes": 0})
Choice.objects.get_or_create(question=q1, choice_text="FastAPI", defaults={"votes": 0})
