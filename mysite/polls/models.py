import datetime

from django.db import models
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text



    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



class Car(models.Model):
    make = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

    def is_new(self):
        return self.year == timezone.now().year