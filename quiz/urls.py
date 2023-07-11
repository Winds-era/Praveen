from django.urls import path
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    quizzes,
    add_quiz,
    update_quiz
)

app_name = 'quiz'

urlpatterns = [
    path('quizzes/', quizzes, name='quizzes'),
    path('add_quiz/', add_quiz, name='add_quiz'),
    path('update-quiz/<int:quiz_id>/', update_quiz, name='update_quiz'),
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
]
