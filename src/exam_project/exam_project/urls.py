"""exam_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from home.views import home_landing
from subscription.views import subscription_view
from register.views import subscribeForm, ChecksubscribeForm
from django.conf.urls import include, url
from useraccount.views import register

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings

from django.urls import include, path
from rest_framework import routers
from api import views
router = routers.DefaultRouter()
router.register(r'Announcement', views.Announcement_Marqee)
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

#from classes.views import view_topic_by_classid
#from exercise.views import start_exercise
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', home_landing, name='home'),
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),),
    path('', include(router.urls)),
    path('home/', home_landing, name='home'),
    path('register/', register, name='register'),
    path('schools/', include('sch.urls')),
    path('ingestion/', include('ingestion.urls')),
    # path('login/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('subscription/', login_required(ChecksubscribeForm), name='subscription'),
    path('exercise/', include('exercise.urls')),
    path('topics/', include('topics.urls')),
    path('exe_questions/', include('exe_questions.urls')),
    path('exercise_result/', include('exercise_result.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#    re_path(r'^topics/(?P<id>[\w-]+)/$', view_topic_by_classid, name="view_topic_by_classid"),
#    re_path(r'^exercise/(?P<id>[\w-]+)/$', login_required(start_exercise), name="start_exercise")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += [
#  path('accounts/', include('django.contrib.auth.urls')),
#url(r'^change_password/$', password_change, {'template_name': 'password_reset_form.html'}, name="password_change"),
#url(r'^change_password_done/$', password_change_done, {'template_name': 'password_reset_done.html'}, name="password_change_done")    
# url('accounts/',(r'^/password_change/$', PasswordResetView, {'template_name': 'registration/password_reset_form.html'})),

#]