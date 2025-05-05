from django.urls import path
from . import views

urlpatterns = [
    path('', views.acid_list, name='acid_list'),
    path('add/', views.add_acid, name='add_acid'),
    path('flashcard/', views.flashcard, name='flashcard'),
    path('quiz/', views.quiz, name='quiz'),
]
