from django.conf.urls import url
from qa.views import *

urlpatterns = [ 
  url(r'^/', get_new_questions),
  url(r'^/popular', get_popular_questions),
  url('^/question/(?P<pk>[0-9]+)', get_question) ]

