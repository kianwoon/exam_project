from django.urls import path
from django.urls import path, re_path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import extract_pdf_2_image, list_all_exam_papers

app_name = 'ingestion'

urlpatterns = [
    path('', login_required(list_all_exam_papers), name='List_all_pdf'),
    # path('extract_pdf/', extract_pdf_2_image, name='extract_pdf'),
    # re_path(r'^(?P<id>[\w-]+)/$', login_required(extract_pdf_2_image), name="extract_pdf"),
    # re_path(r'^(?P<id>[\w-]+)/extract_pdf/$', login_required(extract_pdf_2_image), name="extract_pdf"),
    re_path(r'^extract_pdf/(?P<id>[\w-]+)/$', login_required(extract_pdf_2_image), name="extract_pdf"),
]

# start_exercise