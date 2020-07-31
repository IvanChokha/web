from django.conf.urls import url
from qa.views import *

urlpatterns = [ 
  url(r'^/', get_new_questions),
  url(r'^/popular', get_popular_questions),
  path('^/question/<int:pk>', get_question) ]

