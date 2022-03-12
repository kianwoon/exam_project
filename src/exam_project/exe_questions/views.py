from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ExerciseQuestions
from questions_bank.models import QuestionsBank
from answers_bank.models import AnswersBank
from django.contrib.auth.models import User
from exe_answers.models import ExerciseAnswers
from exe_questions.models import ExerciseQuestions
from exercise.models import ExercisePaper
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.

def answering_question(request, *args, **kwargs):

    if request.method == 'POST':
       
        exercise_paper_id = kwargs.get('id')
        return calculate_result(request, *args, **kwargs)
        #return render(request, 'end_and_calculateresult.html')
    else:
        exercise_id = kwargs.get('id')
        questions_list = ExerciseQuestions.objects.filter(exercise_id=exercise_id)
        form_question = {
            'questions_list' : questions_list,
            'exercise_id' : kwargs.get('id'), 
        }

        return render(request, 'start_exam_exercise.html', form_question)

def calculate_result(request, *args, **kwargs):
    
    exercise_paper_id = kwargs.get('id')
    topic_id = ExercisePaper.objects.filter(exercise_id=exercise_paper_id)
    my_exam_answer_list = ExerciseAnswers.objects.filter(exercise_id=exercise_paper_id)
    
    for exam_question_list in my_exam_answer_list.values():

        Myquestion_id = exam_question_list['question_id_id']
        answerbank_correct_answer = AnswersBank.objects.filter(question_id=Myquestion_id).filter(flag=1)
        question_style = QuestionsBank.objects.filter(question_id=Myquestion_id)
        ques_style = question_style.values_list('styles')[0][0]


        for answerbank_correct_list in answerbank_correct_answer.values():
            print('system answer: ', answerbank_correct_list['answer_id'], answerbank_correct_list['answer_desc'])

            # this is a multiple choices question 
            if ques_style == '1':
                if answerbank_correct_list['answer_id'] == exam_question_list['answer_id_id']:
                    print('answer is CORRECT')
                    # mark the question 
                    ExerciseAnswers.objects.filter(question_id=Myquestion_id).filter(exercise_id=exercise_paper_id).filter(answer_id=exam_question_list['answer_id_id']).update(flag=1)
                    # closed the exercise paper 
                    ExercisePaper.objects.filter(exercise_id=exercise_paper_id).update(status=1)
                    print('this is saved work: ')

            # this is an open text question. sample  '3/4-1/8=6/8-1/8=5/8 5/8-1/3=15/24-8/24=7/24 kg'
            if ques_style == '0':
                myAns = exam_question_list['answer_for_opentext'].replace(' ','').lower()
                if '=' in myAns:
                    myAns = myAns.split('=')
                    myAns = myAns[-1]

                stdAns = answerbank_correct_list['answer_desc'].replace(' ','').lower()
                if '=' in stdAns:
                    stdAns = stdAns.split('=')
                    stdAns = stdAns[-1]

                if stdAns == myAns:
                    # mark the question 
                    ExerciseAnswers.objects.filter(question_id=Myquestion_id).filter(exercise_id=exercise_paper_id).filter(answer_for_opentext=answerbank_correct_list['answer_desc']).update(flag=1)
                        # closed the exercise paper 
                    ExercisePaper.objects.filter(exercise_id=exercise_paper_id).update(status=1)
                    print('answer is CORRECT - 2:')
            

    #return render(request, 'end_and_calculateresult.html')
    return HttpResponseRedirect(reverse('exercise:start_exercise', kwargs={'id': topic_id.values_list('topic_id')[0][0]}))


def display_specific_ques(request, *args, **kwargs):
    
    question_id=kwargs.get('id')
    user_id = request.user 

    exercise_id=request.GET['exercise_id']


    question_value = QuestionsBank.objects.filter(question_id=question_id)
    answer_choices = AnswersBank.objects.filter(question_id=question_id).order_by('answer_desc')

    if request.method == 'POST': # receive answer post by user 

        # delete previous answer submitted by user 
        myquestion = QuestionsBank.objects.get(question_id=question_id)
        myuser = User.objects.get(username=request.user)
        
#        exercise_id = ExerciseQuestions.objects.filter(question_id=question_id).filter(user_id=user_id).values_list('exercise_id')
        

        exercise_name = ExercisePaper.objects.get(exercise_id=exercise_id)

        ExerciseAnswers.objects.filter(question_id=myquestion).filter(user_id=myuser).filter(exercise_id=exercise_id).delete()


        for list in request.POST.getlist('myAnswer'):
            myAnswer = list 
            
            
            # record answer submit by user. this is a multiple choices question 
            if '1' in question_value.values_list('styles')[0]:
                myanswer_m = AnswersBank.objects.get(answer_id=myAnswer)
                ExerciseAnswers.objects.create(question_id=myquestion, user_id=myuser, answer_id=myanswer_m, exercise_id=exercise_name)

            # record answer submit by user. this is a open text or fill in blank question 
            if '0' in question_value.values_list('styles')[0]:
                ExerciseAnswers.objects.create(question_id=myquestion, user_id=myuser, answer_for_opentext=myAnswer, exercise_id=exercise_name)                

    myAns = ExerciseAnswers.objects.filter(question_id=question_id).filter(exercise_id=exercise_id)

    tuple_list = myAns.values_list('answer_id')


    context = {
        'questions_content' : question_value,
        'question_no'  : request.GET['ques_no'], 
        'answer_choices' : answer_choices,
        'myAnswer' : str(tuple_list),
        'myAnswer_for_opentext' : myAns,
        'exercise_id' : exercise_id
    }
    
    return render(request, 'display_specific_ques.html', context)


# http://192.168.1.154:8080/exe_questions/4056e37b-b9e3-4d4c-82a9-c41f4bd4a233/display_specific_ques/


    
    