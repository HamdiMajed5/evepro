from django.contrib import admin
from .models import Category
from judge.models import Judge
from  participant.models import Participant

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

class JudgeAdmin(admin.ModelAdmin):
    pass

class ParticipantAdmin(admin.ModelAdmin):
    pass




admin.site.register(Category,CategoryAdmin)
admin.site.register(Judge,JudgeAdmin)
admin.site.register(Participant,ParticipantAdmin)

