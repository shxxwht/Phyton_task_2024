from django.db import models


class Question(models.Model):
    text = models.TextField()
    def get_correct_answer(self):
        return self.choice_set.get(is_correct = True).text

class Choice(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
   # choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
