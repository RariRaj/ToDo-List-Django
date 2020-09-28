from django.db import models

# Create your models here.
class Task(models.Model):
    objects = models.Manager()
    taskTitle=models.CharField(max_length=30)
    taskDesc=models.TextField()
    taskTime=models.DateTimeField(auto_now_add=True)
    taskCompleted=models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle
    