# forms.py

from django import forms
from .models import Quiz, DIFF_CHOICES

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'topic', 'number_of_questions', 'time', 'required_score_to_pass', 'difficulty']
        widgets = {
            'difficulty': forms.Select(choices=DIFF_CHOICES)
        }
