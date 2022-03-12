from django.core import paginator
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render
from .models import Schools
import pandas as pd

# Create your views here.
def View_School_Primary(request, *args, **kwargs):
    all_school2 = Schools.objects.filter(grade='primary').order_by('school_rank', 'school_name')
    all_school = Paginator(all_school2, 10)
    page_number = request.GET.get('page')
    if not page_number:
        page_number=1
    page_obj = all_school.get_page(page_number)
    
    context = {"schools" : all_school, "grade" : "primary", 'page_obj' : page_obj, 'counter' : 10 * (int(page_number) -1) }
    return render(request, 'all_schools.html', context)

def View_School_Secondary(request, *args, **kwargs):
    all_school2 = Schools.objects.filter(grade='secondary').order_by('-school_rank', 'school_name')
    all_school = Paginator(all_school2, 10)
    page_number = request.GET.get('page')
    if not page_number:
        page_number=1
    page_obj = all_school.get_page(page_number)
    
    context = {"schools" : all_school, "grade" : "primary", 'page_obj' : page_obj, 'counter' : 10 * (int(page_number) -1) }
    return render(request, 'all_schools.html', context)

def Upload_File(request, *args, **kwargs):
    
    data = {}
    if 'GET' == request.method:
        return View_School_Primary(request, *args, **kwargs)
   
    csv_file = request.FILES["csv_file"]
    if not csv_file.name.endswith(".csv"):
        messages.error(request, 'file is not CSV type')
    if csv_file.multiple_chunks():
        messages.error(request, 'Uploaded file is too big')
    
    file_data = csv_file.read().decode('utf-8')
    i=1
    for sch in file_data.splitlines():
        sch2 = str(sch).split('–')
        m2 = Schools(school_name=sch2[0], school_rank=sch2[1], grade='secondary')
        m2.save()
        i+=1
    
   
    return View_School_Primary(request, *args, **kwargs)
