#from django.contrib import admin
import autocomplete_all as admin
from .models import Category, Evaluation , Participant ,Teacher , Judge
from django.db.models import F, ExpressionWrapper, DecimalField, Subquery, Sum, Value
from django.shortcuts import render , HttpResponse ,HttpResponseRedirect, redirect ,reverse

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    search_fields=[
        'name'
    ]


class JudgeAdmin(admin.ModelAdmin):
    search_fields = [
        'name'
    ]


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
        'age',
        'student_total',
        'parent_total',
        'teacher_total',
        'total'
    ]

    def total(self, obj):
        return obj.total

    def student_total(self, obj):
        return obj.student_total

    def parent_total(self, obj):
        return obj.parent_total

    def teacher_total(self, obj):
        return obj.teacher_total

    total.admin_order_field = 'total'
    student_total.admin_order_field = 'student_total'
    parent_total.admin_order_field = 'parent_total'
    teacher_total.admin_order_field = 'teacher_total'

    def get_queryset(self, request):
        qs = super(ParticipantAdmin, self).get_queryset(request)
        qs = qs.annotate(
            total=ExpressionWrapper(
                Sum('evaluation__student_mark') + Sum('evaluation__parent_mark') + Sum('evaluation__teacher_mark')
                , output_field=DecimalField()),
            student_total=Sum('evaluation__student_mark'),
            parent_total=Sum('evaluation__parent_mark'),
            teacher_total=Sum('evaluation__teacher_mark')
        )
        return qs


class EvaluationAdmin(admin.ModelAdmin):

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect(reverse('qrcode:scan'))

    def response_change(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect(reverse('qrcode:scan'))


class TeacherAdmin(admin.ModelAdmin):
    search_fields = [
        'name'
    ]
    list_display = [
        'name',
        'total'
    ]

    def total (self,obj):
        return obj.total

    def get_queryset(self, request):
        qs = super(TeacherAdmin, self).get_queryset(request)
        qs=qs.annotate(total=Sum('participant__evaluation__teacher_mark'))
        return qs

admin.site.register(Category, CategoryAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(Teacher,TeacherAdmin)
