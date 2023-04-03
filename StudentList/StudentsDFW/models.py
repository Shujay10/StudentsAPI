from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    grade = models.IntegerField()
    regno = models.IntegerField()
