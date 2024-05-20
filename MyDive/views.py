from django.shortcuts import redirect, render

from .models import Choice, Question

articles = [
   {
       'id': 1,
       'title': 'First news',
       'text': 'This is the worst first article'
   },
   {
       'id': 2,
       'title': 'Second news',
       'text': 'This is the amazing second article'
   }]
questions = [
        {
            'question_text': 'Давление, действующее на аквалангиста на глубине 20м равно',
            'choices': [
                {'choice_text': '2 атмосферам', 'percentage': '13%'},
                {'choice_text': '3 атмосферам', 'percentage': '66%'},
                {'choice_text': '4 атмосферам', 'percentage': '13%'},
                {'choice_text': '1 атмосфере', 'percentage': '8%'},
            ]
        }
        # ... добавьте остальные вопросы
    ]
# Create your views here.
def index(request):
    return render(request, "MyDive/base.html",{'articles':articles})
def registration(request):
    return render(request, 'MyDive/registration.html')

#def quiz_view(request):
    #return render(request, "MyDive/quiz.html", {'questions': questions})

def quiz(request):
    questions = Question.objects.all()
    return render(request, 'MyDive/quiz.html', {'questions': questions})
def submit_quiz(request):
       if request.method == 'POST':
           score = 0
           for question in Question.objects.all():
               selected_choice_id = request.POST.get(f'question_{question.id}')
               if selected_choice_id:
                   selected_choice = Choice.objects.get(id=selected_choice_id)
                   if selected_choice.is_correct:
                       score += 1
           return render(request, 'MyDive/results.html', {'score': score})
       return redirect('quiz')
