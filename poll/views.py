from django.shortcuts import render
from poll.models import Question,Choice
# Create your views here.
from django.http import HttpResponse
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join(q.question_text for q in latest_question_list)
    return HttpResponse(output)

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request,question_id):
    return HttpResponse("You're looking at results of question %s" % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting at question %s" % question_id)




