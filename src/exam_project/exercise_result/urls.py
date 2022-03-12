from django.urls import path
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from .views import list_exercise_result

app_name = 'exercise_result'

urlpatterns = [
#    path('', answering_question, name='answering_question'),
#    re_path(r'^(?P<id>[\w-]+)/$', login_required(answering_question), name="answering_question"),
    re_path(r'^(?P<id>[\w-]+)/list_exercise_result/$', login_required(list_exercise_result), name="list_exercise_result"),

]

# start_exercise