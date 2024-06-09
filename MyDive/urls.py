from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),

       path('registration/', views.registration, name='registration'),
       path('quiz/', views.quiz, name='quiz'),
       path('instruction/', views.instruction_view, name='instruction'),
       path('study/', views.study, name='study'),
       path('dive_world/', views.dive_world, name='dive_world'),
       #path('submit_quiz/', views.submit_quiz, name='submit_quiz'),
       #path('submit_answer/<int:question_id>/', views.submit_answer, name='submit_answer'),
]