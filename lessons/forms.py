from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['subject', 'grade', 'day', 'start_time', 'end_time']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masalan, Matematika'}),
            'grade': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Sinf'}),
            'day': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Kun'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'placeholder': 'Boshlanish'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'placeholder': 'Tugash'}),
        }
        labels = {
            'subject': "Dars (fan) nomi",
            'grade': "Sinf",
            'day': "Hafta kuni",
            'start_time': "Boshlanish vaqti",
            'end_time': "Tugash vaqti",
        }