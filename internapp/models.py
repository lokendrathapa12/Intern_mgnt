from django.db import models

# Create your models here.
from email.utils import make_msgid
from pyexpat import model
from django.db import models

# Create your models here.
class Attendence (models.Model):
    presant_choices=[
        ('presant','presant'),
        ('abscent','abscent')
        ]
    attend = models.CharField(max_length=50,choices=presant_choices,default="")
    name = models.CharField(max_length=100,default="")
    date = models.DateField(default=" ")
    def __str__(self):
        return self.name

class task (models.Model):
    task_heading = models.CharField(max_length=500)
    task_description = models.TextField(max_length=4000)
    note = models.CharField(max_length=1000)
    belongs_to = models.CharField(max_length=70)

    def __str__(self):
        return self.task_heading

class TaskSubmit(models.Model):
    fullname = models.CharField(max_length=70)
    taskname = models.CharField(max_length=70)
    taskfile = models.FileField(upload_to='image/')