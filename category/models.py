from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Evaluation (models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    participant=models.ForeignKey('participant.participant',on_delete=models.CASCADE)
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


