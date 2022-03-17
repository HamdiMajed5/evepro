from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Judge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.category.name}'


class Teacher(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.name

class Participant(models.Model):
    qrid=models.IntegerField(unique=True)
    name=models.CharField(max_length=60)
    age=models.IntegerField(null=True,blank=True)
    phone=models.CharField(max_length=60 , blank=True,null=True)
    teacher_name=models.ForeignKey(Teacher, on_delete=models.DO_NOTHING,blank=True,null=True)

    def grand_total(self):
        evals=Evaluation.objects.filter(participant=self)
        if evals :
            evals= evals.aggregate(Sum('student_mark'),Sum('parent_mark'),Sum('teacher_mark'))
            student_total = evals['student_mark__sum']
            parent_total = evals['parent_mark__sum']
            teacher_total = evals['teacher_mark__sum']
            return student_total+parent_total+teacher_total
        return 0
    def student_total(self):
        evals=Evaluation.objects.filter(participant=self)
        if evals:
            evals= evals.aggregate(Sum('student_mark'),Sum('parent_mark'),Sum('teacher_mark'))
            student_total = evals['student_mark__sum']
            return student_total
        return 0
    def parent_total(self):
        evals=Evaluation.objects.filter(participant=self)
        if evals:
            evals= evals.aggregate(Sum('student_mark'),Sum('parent_mark'),Sum('teacher_mark'))
            parent_total = evals['parent_mark__sum']
            return parent_total
        return 0

    def teacher_total(self):
        evals=Evaluation.objects.filter(participant=self)
        if evals:
            evals= evals.aggregate(Sum('student_mark'),Sum('parent_mark'),Sum('teacher_mark'))
            teacher_total = evals['teacher_mark__sum']
            return teacher_total
        return 0


    grand=property(grand_total)
    student=property(student_total)
    parent=property(parent_total)
    teacher=property(teacher_total)


    def __str__(self):
        return self.name


class Evaluation (models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    participant=models.ForeignKey(Participant,on_delete=models.CASCADE)
    student_mark=models.IntegerField(choices=(
        (0,0),
        (1,1),
        (2,2),
        (3,3)
    ),default=0)
    parent_mark=models.IntegerField(choices=(
        (0, 0),
        (1,1),
        (2,2)
    ),default=0)
    teacher_mark = models.IntegerField(choices=(
        (0, 0),
        (1, 1)
    ),default=0)
    note=models.CharField(max_length=255,blank=True)

    def total(self):
        return self.student_mark+self.parent_mark+ self.teacher_mark

    total=property(total)

    def __str__(self):
        return f"{self.participant.name} - {self.category.name} ({self.total})"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category', 'participant'], name="participant_already_evaluated")
        ]

