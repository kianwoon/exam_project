from django.urls import path
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from classes.views import view_topic_by_classid

app_name = 'topics'

urlpatterns = [
    re_path(r'^(?P<id>[\w-]+)/$', login_required(view_topic_by_classid), name="view_topic_by_classid"),
]