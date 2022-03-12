from django.urls import path
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from .views import answering_question, display_specific_ques

app_name = 'exe_questions'

urlpatterns = [
#    path('', answering_question, name='answering_question'),
#    re_path(r'^(?P<id>[\w-]+)/$', login_required(answering_question), name="answering_question"),
    re_path(r'^(?P<id>[\w-]+)/answering_question/$', login_required(answering_question), name="answering_question"),
    re_path(r'^(?P<id>[\w-]+)/display_specific_ques/$', login_required(display_specific_ques), name="display_specific_ques"),

]

# start_exercise