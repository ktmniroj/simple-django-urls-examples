from django.http import HttpResponse
from django.shortcuts import render
from . models import Question, Choice

def index(request):
	all_question = Question.objects.all()
	# html = ''
	# for question in all_question:
	# 	html += str(question.id)+'. ' + str(question) +'<br>'
	# return HttpResponse(html)

	context = {
    	'all_question': all_question,
    }
	return render(request, 'polls/index.html',context)

 
def detail(request, question_id):
	return HttpResponse("<h1> The id of this question is:  %s " % question_id +"</h1>")

def results(request, question_id):
	all_choice = Choice.objects.get(pk= question_id)
	http = ''
	http += "The answer of this question is: "+ str(all_choice.choice_text) 
	return HttpResponse(http)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
