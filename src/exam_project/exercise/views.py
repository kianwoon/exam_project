from django.shortcuts import render, redirect
from django.http import HttpResponse
from topics.models import Topics 
from classes.models import Classes
from exercise.models import ExercisePaper
from django.contrib.auth.models import User
from register.models import UserSubscription 
import datetime 
from django.contrib import messages
from django.db import connection 
from exe_questions.models import ExerciseQuestions
from questions_bank.models import QuestionsBank
from django.urls import reverse

# Create your views here.

# This is the landing 
def start_exercise(request, *args, **kwargs):

    if request.method == 'POST':
        content = {
            "topic_id" : kwargs, 
            "username" : request.user
        }
  #create a new exercise 
 
        create_exercise(request, content)
        return start_preparing_exercise(request, *args, **kwargs)
    else:
        return start_preparing_exercise(request, *args, **kwargs)

# list all exercises  
def start_preparing_exercise(request, *args, **kwargs):
    topic_name = Topics.objects.filter(topic_id=kwargs['id'])
    # list of pending exercise 
    list_of_exercise = ExercisePaper.objects.filter(user_id=request.user).filter(topic_id=kwargs.get('id')).filter(status=0).order_by('exercise_date')
 
    context = {
            "topic_name" : topic_name[0],
            "topic_id" : kwargs,
            "exercises_list" : list_of_exercise
    }
    return render(request, 'start_exercise.html', context)


# generate a new exercise_paper records
def create_exercise(request, *args, **kwargs):
    today = datetime.datetime.now()
    user_sub_status = UserSubscription.objects.filter(username=request.user).filter(subscription_end__gte=today)
    list_of_exercise = ExercisePaper.objects.filter(user_id=request.user).filter(topic_id=args[0].get('topic_id').get('id')).filter(status=0)

    if user_sub_status and list_of_exercise.count() < 3:
        user_id = User.objects.get(username=request.user)
        topic_id = Topics.objects.get(topic_id=args[0].get('topic_id').get('id'))
        ExercisePaper.objects.create(user_id=user_id, topic_id=topic_id)
    elif user_sub_status and list_of_exercise.count() > 2:
        messages.success(request,'Maximum exercise allowed is 3. Please finsih first before create new one.')
    else:
        messages.success(request,'Please activate your subscription first')


def start_loading_questions(request, *args, **kwargs):
    return reverse('exe_questions:answering_question')


def loading_questions(request, *args, **kwargs):
    exercises_id = ExercisePaper.objects.filter(exercise_id=kwargs.get('id'))
    exe_id = ExercisePaper.objects.get(exercise_id=kwargs.get('id'))


    topic_id=exercises_id.values_list('topic_id')[0][0].hex
    cursor = connection.cursor() 
    user_id = request.user

    cursor.execute("select qb.question_id from examdb.exercise_questions eq right join examdb.questions_bank qb on eq.question_id = qb.question_id where ((eq.question_id is null) and (qb.topic_id = %s)) and (eq.user_id is null or eq.user_id <> %s) order by RAND() limit 10", [topic_id, user_id])
    user_id = User.objects.get(username=request.user)

    print('topic id:', topic_id)
    

    if not ExerciseQuestions.objects.filter(exercise_id=exe_id):

        i = 0
        mylist1 = cursor.fetchall()

        for row in mylist1:
            i = i + 1
            ques_id = QuestionsBank.objects.get(question_id=row[0])
            ExerciseQuestions.objects.create(user_id=user_id, exercise_id=exe_id, question_id=ques_id)
        
        # this logic is to prevent user has finish all questions in the system. recycle 

        if i < 10:

            cursor.execute("select qb.question_id from examdb.questions_bank qb where (qb.topic_id = %s) order by RAND() limit %s", [topic_id, 10-i])
            mylist2 = cursor.fetchall()
            print('this is manual cursor 2:', mylist2)
            print('===============')
            print('hello 2 ')
            for row in mylist2:
                ques_id = QuestionsBank.objects.get(question_id=row[0])
                ExerciseQuestions.objects.create(user_id=user_id, exercise_id=exe_id, question_id=ques_id)
    
# start answering questions
    return redirect('exe_questions:answering_question', kwargs.get('id'))
    
