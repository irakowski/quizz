from django.contrib import admin
from django.urls import path, include
from . import views as quiz_views

app_name = 'quiz'

urlpatterns = [
   path('',quiz_views.CategoryView.as_view(), name='categories'),
   path('<str:slug>/', quiz_views.CategoryDetail.as_view(), name='questions'),
   path('<slug>/<pk>', quiz_views.QuestionView.as_view(), name='question'),
]