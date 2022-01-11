# <<polls.views>>------------------------
from django.shortcuts import render, get_object_or_404
from polls.models import Question
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    question_list = Question.objects.all().order_by('-pub_date')
    context = {'my_list' : question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'my_question': question}
    return render(request, 'polls/detail.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes +=1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results',
                                        args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'my_question': question}
    return render(request, 'polls/results.html', context)

def bulletin(request):
    bulletin_list = Bulletin.objects.all().order_by('-b_date')
    context = {'bulletin_context' : bulletin_list}
    return render(request, 'polls/../bulletin/templates/bulletin/bulletin.html', context)

