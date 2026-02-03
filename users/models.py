from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    Role_Choices = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('director', 'BIG_BOSS')
    )
    role = models.CharField(max_length = 20, choices=Role_Choices, default='student')
    GRADES = (
        ('1', '1-sinf'),
        ('2', '2-sinf'),
        ('3', '3-sinf'),
        ('4', '4-sinf'),
        ('5', '5-sinf'),
        ('6', '6-sinf'),
        ('7', '7-sinf'),
        ('8', '8-sinf'),
        ('9', '9-sinf'),
        ('10', '10-sinf'),
        ('11', '11-sinf'),
    )
    grade = models.CharField(max_length=10, choices=GRADES, blank=True, null=True)