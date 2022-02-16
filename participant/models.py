from django.db import models
from category.models import Evaluation
from django.db.models import Sum
# Create your models here.

class Participant(models.Model):
    qrid=models.IntegerField(unique=True)
    name=models.CharField(max_length=60)
    age=models.IntegerField(null=True,blank=True)
    phone=models.CharField(max_length=60)

    def grand_total(self):
        evals=Evaluation.objects.filter(participant=self)
        evals= evals.aggregate(Sum('student_mark'),Sum('parent_mark'),Sum('teacher_mark'))
        student_total = evals['student_mark__sum']
        parent_total = evals['parent_mark__sum']
        teacher_total = evals['teacher_mark__sum']
        return student_total+parent_total+teacher_total

    def student_total(self):
        evals=Evaluation.objects.filter(participant=self)
        evals= evals.aggregate(Sum('student_mark'),Sum('parent_mark'),Sum('teacher_mark'))
        student_total = evals['student_mark__sum']
        return student_total

    def parent_total(self):
        evals=Evaluation.objects.filter(participant=self)
        evals= evals.aggregate(Sum('student_mark'),Sum('parent_mark'),Sum('teacher_mark'))
        parent_total = evals['parent_mark__sum']
        return parent_total

    def teacher_total(self):
        evals=Evaluation.objects.filter(participant=self)
        evals= evals.aggregate(Sum('student_mark'),Sum('parent_mark'),Sum('teacher_mark'))
        teacher_total = evals['teacher_mark__sum']
        return teacher_total



    grand=property(grand_total)
    student=property(student_total)
    parent=property(parent_total)
    teacher=property(teacher_total)


    def __str__(self):
        return self.name



