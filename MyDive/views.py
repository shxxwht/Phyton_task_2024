from django.shortcuts import render

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
# Create your views here.
def index(request):
    return render(request, "MyDive/base.html",{'articles':articles})
def registration(request):
    return render(request, 'MyDive/registration.html')
def quiz(request):
    return render(request, 'MyDive/quiz.html')
def instruction_view(request):
    return render(request, 'MyDive/instruction.html')
def dive_world(request):
    return render(request, 'MyDive/dive_world.html')
def study(request):
    return render(request, 'MyDive/study.html')