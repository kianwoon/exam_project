from django.contrib import admin
from .models import QuestionsBank
from answers_bank.models import AnswersBank

# Register your models here.
class AnswersBankForm(admin.StackedInline):
    model = AnswersBank
    extra = 0


class QuestionsBankForm(admin.ModelAdmin):
    inlines = [AnswersBankForm]


admin.site.register(QuestionsBank, QuestionsBankForm)