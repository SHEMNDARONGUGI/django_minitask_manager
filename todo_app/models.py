from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=30 ,default='', blank=False)
    description = models.CharField(max_length=100 ,default='', blank=True)

    def __str__(self):
        return self.task_name