from django.http import HttpResponse
from django.shortcuts import render
from classes.models import Classes
from register.models import UserSubscription
import datetime 
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from web_content.models import WebContent

# Create your views here.
def home_landing(request, *args, **kwargs):

    if not request.user.is_authenticated:
        WebData = WebContent.objects.filter(status=1, auth_group=0)
        context = {
            'web_content' : WebData
        }
        return render(request, "home.html", context)
    else:
        
        registered_user = UserSubscription.objects.filter(username=request.user, subscription_end__gte=datetime.datetime.today())
        if registered_user:
            class_id = registered_user.values_list("class_id")[0][0]    
            return HttpResponseRedirect(reverse('topics:view_topic_by_classid', kwargs={'id': class_id}))
        else:
            WebData = WebContent.objects.filter(status=1, auth_group=1)
            schools = Classes.objects.all().order_by('class_description')
            context = {
                'web_content' : WebData,
                'schools' : schools
            }            
            
            schools_id = Classes.objects.all()
            return render(request, "home.html", context)


 

 