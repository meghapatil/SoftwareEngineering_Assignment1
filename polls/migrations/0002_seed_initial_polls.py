from django.db import migrations
from django.utils import timezone

def create_initial_polls(apps, schema_editor):
    Question = apps.get_model('polls', 'Question')
    Choice = apps.get_model('polls', 'Choice')

    # First question
    q1, created = Question.objects.get_or_create(
        question_text="Which framework do you like most?",
        defaults={"pub_date": timezone.now()},
    )
    if created or not Choice.objects.filter(question=q1).exists():
        Choice.objects.get_or_create(question=q1, choice_text="Django", defaults={"votes": 0})
        Choice.objects.get_or_create(question=q1, choice_text="Flask", defaults={"votes": 0})
        Choice.objects.get_or_create(question=q1, choice_text="FastAPI", defaults={"votes": 0})

    # Second question
    q2, created = Question.objects.get_or_create(
        question_text="What’s your favorite programming language?",
        defaults={"pub_date": timezone.now()},
    )
    if created or not Choice.objects.filter(question=q2).exists():
        Choice.objects.get_or_create(question=q2, choice_text="Python", defaults={"votes": 0})
        Choice.objects.get_or_create(question=q2, choice_text="Java", defaults={"votes": 0})
        Choice.objects.get_or_create(question=q2, choice_text="JavaScript", defaults={"votes": 0})

class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0001_initial'),  # change if your previous migration has a different name
    ]

    operations = [
        migrations.RunPython(create_initial_polls),
    ]