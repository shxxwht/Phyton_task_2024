from django import forms

from .models import Choice


class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ModelChoiceField(
                queryset=Choice.objects.filter(question=question),
                widget=forms.RadioSelect,
                label=question.question_text
            )