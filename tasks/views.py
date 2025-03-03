from django.shortcuts import render
from django import forms


tasks = ["1", '2', '3']

class newTaskForm(forms.Form):
    task = forms.CharField(label="New task")
    priority = forms.IntegerField(label="priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html", {
        "form": newTaskForm()
    })
