from django.db import models


class Employee_skill(models.Model):
    emp_id = models.IntegerField()
    skills = models.CharField(max_length=100)
    percentage = models.IntegerField()
