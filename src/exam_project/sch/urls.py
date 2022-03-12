from django.urls import path
from django.urls import path, re_path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import View_School_Primary, Upload_File, View_School_Secondary

app_name = 'sch'


urlpatterns = [
    path('all_primary/', View_School_Primary, name='all_primary'),
    path('all_secondary/', View_School_Secondary, name='all_secondary'),
    url(r'^upload/$', Upload_File, name='upload_csv'),
]

# start_exercise