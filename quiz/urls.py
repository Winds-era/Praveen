from django.urls import path
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    quizzes,
    add_quiz,
    update_quiz,
    delete_quiz,
    question_list,
    add_question,
    delete_question,
    update_question,
)

app_name = 'quiz'

urlpatterns = [
    path('quizzes/', quizzes, name='quizzes'),
    path('add_quiz/', add_quiz, name='add_quiz'),
    path('update-quiz/<int:quiz_id>/', update_quiz, name='update_quiz'),
    path('delete-quiz/<int:quiz_id>/', delete_quiz, name='delete_quiz'),
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('question-list/<int:quiz_id>/', question_list, name='question_list'),
    path('add-question/<int:quiz_id>/', add_question, name='add_question'),
    path('delete-question/<int:question_id>/', delete_question, name='delete_question'),
    path('update-question/<int:question_id>/', update_question, name='update_question'), 
]
