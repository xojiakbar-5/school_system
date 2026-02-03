from django.db import models
from django.conf import settings


class Lesson(models.Model):
    Days_OF_WEEK = (
        ('Mon', 'Dushanba'),
        ('Tues', 'Seshanba'),
        ('Wednes', 'Chorshanba'),
        ('Thurs', 'Payshanba'),
        ('Fri', 'JUMA'),
        ('Satur', 'Shanba'),
        ('Sun', 'Yakshanba'),
    )
    
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

    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, choices=GRADES, blank=True, null=True)

    day = models.CharField(max_length=10, choices=Days_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.subject
    
class ActionLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action} - {self.subject}"
