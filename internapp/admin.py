from django.contrib import admin
from .models import Attendence, TaskSubmit, task
# Register your models here.
#admin.site.register(Attendence)
#admin.site.register(task)
@admin.register(Attendence)
class AttendenceAdminModel(admin.ModelAdmin):
    list_display = ('id','attend','name','date')
@admin.register(task)
class TaskAdminModel(admin.ModelAdmin):
    list_display = ('id','task_heading','task_description','note','belongs_to')
@admin.register(TaskSubmit)
class FileAdminModel(admin.ModelAdmin):
    list_display = ('id','fullname','taskname','taskfile')