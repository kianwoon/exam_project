from django.urls import path
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from .views import start_exercise, start_preparing_exercise, start_exercise, start_loading_questions, loading_questions

app_name = 'exercise'

urlpatterns = [
    re_path(r'^(?P<id>[\w-]+)/$', login_required(start_exercise), name="start_exercise"),
    re_path(r'^(?P<id>[\w-]+)/start_preparing_exercise/$', login_required(start_preparing_exercise), name="start_preparing_exercise"),
    re_path(r'^(?P<id>[\w-]+)/start_exercise/$', login_required(start_exercise), name="start_exercise"),
    re_path(r'^(?P<id>[\w-]+)/loading_questions/$', login_required(loading_questions), name="loading_questions"),

]

# start_exercise