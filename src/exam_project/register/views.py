from django.shortcuts import render
from .forms import subscription_form
from .models import UserSubscription 
from django.contrib import messages
from classes.models import Classes
#=======================
from django.contrib.auth.models import User 
from subscription.models import Subscription 
from datetime import date 
import re
from dateutil.relativedelta import relativedelta
#=======================

from django.utils import timezone

# Create your views here.

def subscribeForm(request, plan_id, plan_duration, class_level):
   form = subscription_form(request.POST or None)
   subscription_plan = Subscription.objects.all().order_by("title")


   if request.method == 'POST':
      
      if len(class_level) <= 20:
         messages.warning(request, 'Please select your class')   
         form=subscription_form()
         class_level = Classes.objects.all().order_by("class_level")
         context = {'form': form, "plan" : subscription_plan, "class" : class_level }
         return render(request, "subscription.html", context)

      
      subsc_date = date.today()
      subsc_end_date = date.today() + relativedelta(months=+int(plan_duration))
      username = User.objects.get(username=request.user)
      plan=Subscription.objects.get(subscription_id=plan_id)
      # print('\n\nhi 3\n\n')
      class_id = Classes.objects.get(class_id=class_level)
      # print('\n\nhi 2\n\n')

      try: 
         UserSubscription.objects.create(subscription_id=plan, username=username, subscription_date=subsc_date, subscription_end=subsc_end_date, class_id=class_id)
         
         messages.success(request, 'Subscription activated.')
         return ChecksubscribeForm(request)
      except:
         if not class_id:
            messages.warning(request, 'Please select your class')   
         else:
            messages.warning(request, 'Subscription is still valid.')

   form=subscription_form()
   class_level = Classes.objects.all().order_by("class_level")
   context = {'form': form, "plan" : subscription_plan, "class" : class_level }
   return render(request, "subscription.html", context)


def ChecksubscribeForm(request, *args, **kwargs):
      today = timezone.now()
      subscription_plan = Subscription.objects.all().order_by("title") 
      user_sub_status = UserSubscription.objects.filter(username=request.user).filter(subscription_end__gte=today)
      
      plan_id = request.POST.get('plan_id')
      plan_duration = request.POST.get('plan_duration')
      class_level = request.POST.get('class_level')

      if user_sub_status:
         user_sub_end_date = user_sub_status.values_list('subscription_end')[0][0].strftime("%d-%B-%Y")
#         messages.success(request, 'Subscription is valid until %s' %  user_sub_end_date)
         context= {'subscription_enddate' :  user_sub_end_date, 'plan' : subscription_plan}
         return render(request, 'subscription_valid.html', context)
      else:
         
         return subscribeForm(request, plan_id, plan_duration, class_level)

   
