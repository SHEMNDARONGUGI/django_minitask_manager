from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(default='', blank=False)
    description = models.CharField(default='', blank=True)

    def __str__(self):
        return self.task_name