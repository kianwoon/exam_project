from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection 
from exe_questions.models import ExerciseQuestions
from exe_answers.models import ExerciseAnswers
from exercise.models import ExercisePaper

# Create your views here.
def list_exercise_result(request, *args, **kwargs):
    exercise_id = kwargs['id']
    exercise_questions_list = ExerciseQuestions.objects.filter(exercise_id=exercise_id)
    exercise_answers_list = ExerciseAnswers.objects.filter(exercise_id=exercise_id)
    num_of_wrong_answer =  ExerciseAnswers.objects.values('question_id').distinct().filter(exercise_id=exercise_id).filter(flag=0).count()
    num_of_answered_question = ExerciseAnswers.objects.values('question_id').distinct().filter(exercise_id=exercise_id).count()
    num_of_not_answered = exercise_answers_list.count() - num_of_answered_question


    result = '{} / {}'.format(exercise_answers_list.count() - num_of_wrong_answer - num_of_not_answered, exercise_questions_list.count())
    result_mark = ((exercise_answers_list.count() - num_of_wrong_answer - num_of_not_answered) / exercise_questions_list.count()) * 100
    ExercisePaper.objects.filter(exercise_id=exercise_id).update(result=result_mark)

    cursor = connection.cursor() 
    cursor.execute("select ab.question_id, ab.answer_desc from examdb.exercise_questions eq inner join examdb.answers_bank ab on ab.question_id = eq.question_id where eq.exercise_id = %s and ab.flag = 1;", [exercise_id.replace('-','')])
    mylist1 = cursor.fetchall()


    context = {
        'exercise_question' : exercise_questions_list,
        'exercise_answer' : exercise_answers_list,
        'correct_answer' : mylist1,
        'result' : result
    }
    

    
    return render(request, 'completed_and_result.html', context)