from django.shortcuts import render
from django.http import HttpResponse
from topics.models import Topics
from register.models import UserSubscription
import datetime 
from classes.models import Classes
from exercise.models import ExercisePaper
from topics.models import Topics
# Create your views here.

def view_topic_by_classid(request, *args, **kwargs):
    # to preset the class for the registered + subscribed user. go direct to topic 
    
    registered_user = UserSubscription.objects.get(username=request.user, subscription_end__gte=datetime.datetime.today())
    
    if registered_user:
        if len(str(registered_user.class_id.class_id)) < 36:
            registered_user.class_id=kwargs.get('id')
            registered_user.save()
    
    class_level = Classes.objects.get(class_id=kwargs.get('id'))
    topic_name = Topics.objects.filter(class_id=kwargs.get('id')).filter(status=1)
    
    topic_dict = {
        'topics' : topic_name,
        'class_desc' : class_level.class_description,
        'exercise_paper_list_completed' : view_exercise_paper_completed(request)
    }
    return render(request, 'view_topic_by_class.html', topic_dict)


def view_exercise_paper_completed(request, *args, **kwargs):
    exercise_list = ExercisePaper.objects.filter(user_id=request.user).filter(status=1)
    return exercise_list 


