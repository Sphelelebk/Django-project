
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader, RequestContext
from .models import Question
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question': latest_questions}
    return render(request, 'polls/index.html', context)

    return HttpResponse(template.render(context))

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse("These are the result of the question: %s " % question_id)

def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)

