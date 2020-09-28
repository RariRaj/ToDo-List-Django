from django.forms import ModelForm
from home.models import Task

class ListForm(ModelForm):
    class Meta:
        model = Task
        fields= ["taskTitle","taskDesc","taskCompleted"]


        