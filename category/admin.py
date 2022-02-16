from django.contrib import admin
from .models import Category , Evaluation
from judge.models import Judge
from  participant.models import Participant
from django.db.models import F, ExpressionWrapper, DecimalField

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

class JudgeAdmin(admin.ModelAdmin):
    pass

class ParticipantAdmin(admin.ModelAdmin):
    readonly_fields = [
        'student',
        'parent',
        'teacher',
        'grand'
    ]
    search_fields = [
        'qrid',
        'name'
    ]
    list_display = [
        'qrid',
        'name',
        'student',
        'parent',
        'teacher',
        'grand'
    ]

    

class EvaluationAdmin (admin.ModelAdmin):
    pass



admin.site.register(Category,CategoryAdmin)
admin.site.register(Judge,JudgeAdmin)
admin.site.register(Participant,ParticipantAdmin)
admin.site.register(Evaluation,EvaluationAdmin)

