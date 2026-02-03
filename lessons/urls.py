from django.urls import path
from . import views

urlpatterns = [
    path('jadval/', views.timetable, name='timetable'),
    path('jadval/qoshish/', views.lesson_create, name='lesson_create'),
    path('jadval/tahrirlash/<int:pk>/', views.lesson_update, name='lesson_update'),
    path('jadval/ochirish/<int:pk>/', views.lesson_delete, name='lesson_delete'),
    path('jadval/tarix/', views.action_history, name='action_history'),
]