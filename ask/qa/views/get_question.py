from django.http import Http404
from django.shortcuts import render
from ..models import Question
from ..models import Answer

def get_question(request, pk):
  try:
    question = Qestion.get(pk)
  except Question.DoesNotExist:
    raise Http404
  answers = Answer.objects.filter(question=question)
  return render(request, 'question.html', {
        'question': question,
        'answers': answers

  })
