from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Lesson(models.Model):
    class Days(models.TextChoices):
        MONDAY = 'Mon', _('Dushanba')
        TUESDAY = 'Tues', _('Seshanba')
        WEDNESDAY = 'Wednes', _('Chorshanba')
        THURSDAY = 'Thurs', _('Payshanba')
        FRIDAY = 'Fri', _('Juma')
        SATURDAY = 'Satur', _('Shanba')
        SUNDAY = 'Sun', _('Yakshanba')

    class Grades(models.TextChoices):
        GRADE_1 = '1', _('1-sinf')
        GRADE_2 = '2', _('2-sinf')
        GRADE_3 = '3', _('3-sinf')
        GRADE_4 = '4', _('4-sinf')
        GRADE_5 = '5', _('5-sinf')
        GRADE_6 = '6', _('6-sinf')
        GRADE_7 = '7', _('7-sinf')
        GRADE_8 = '8', _('8-sinf')
        GRADE_9 = '9', _('9-sinf')
        GRADE_10 = '10', _('10-sinf')
        GRADE_11 = '11', _('11-sinf')

    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, choices=Grades.choices, blank=True, null=True)

    day = models.CharField(max_length=10, choices=Days.choices)
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
