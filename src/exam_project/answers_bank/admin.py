from django.contrib import admin
from .models import AnswersBank
# Register your models here.
class AnswersBankForm(admin.ModelAdmin):
    list_display = ['answer_desc']
    search_fields = ['answer_desc']

#admin.site.register(AnswersBank, AnswersBankForm)