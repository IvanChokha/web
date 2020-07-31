from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import Question

def get_new_questions(request):
  page = request.GET.get('page', 1)
  questions = Qestion.objects.order_by('-id')
  paginator = Paginator(questions, 10)
  paginator.baseurl = '/'
  return render(request, 'question_list.html', {
        'questions': questions,
        'paginator': paginator,
        'page': page,
  })
