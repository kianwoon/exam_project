from django.shortcuts import render
from .models import Subscription
from classes.models import Classes
from django.contrib.auth.decorators import login_required


@login_required

# Create your views here.

def subscription_view(request, *args, **kwargs):
     
     subscription_plan = Subscription.objects.all() 
     class_level = Classes.objects.all().order_by("class_level")
     
     
     context = {
          "plan" : subscription_plan,
          "class" : class_level
     }
     return render(request, "subscription.html", context)

