from django.shortcuts import render, get_object_or_404
from poll.models import Question,Choice
from django.urls import reverse 
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list' : latest_question_list}
    return render(request, 'poll/index.html', context)

def detail(request,question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id) #get_ist_or_404()
    return render(request, 'poll/detail.html', {'question':question})

def results(request,question_id):
    question = get_object_or_404(Question, pk= question_id)
    return render(request, 'poll/results.html', {"question": question})

def vote(request,question_id):
    question = get_object_or_404(Question, pk= question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "poll/detail.html", {"question": question, "error_message": "You did not select a choice" })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("poll:results", args = (question.id,)))
    return HttpResponse("You're voting at question %s" % question_id)




