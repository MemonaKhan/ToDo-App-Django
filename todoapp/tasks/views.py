from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.http import HttpResponseRedirect    # for redirecting page


# from django import forms            # for django forms added


from .models import *
from .forms import *

# class NewTasksForm(forms.Form):
    # title = forms.CharField(label="New Task")

# Create your views here.

# handling viewing tasks and creating tasks

def index(request):
    # return HttpResponse("Hello Here")
	tasks = Task.objects.all()                 # getting all data from model

	form = TaskForm()                          # getting form fields from modelForm

	if request.method =='POST':                  # handling post reuqest from creating tasks
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/tasks')
        # return HttpResponseRedirect(reverse("tasks/list.html"))  # but after giving appname use tasks:index here



	# context = {'tasks':tasks}
	context = {'tasks':tasks, 'form':form}
	return render(request, 'tasks/list.html', context)       # here handling read data
	# return render(request, 'tasks/list.html')


# handling updating tasks

def updateTask(request, pk):
	task = Task.objects.get(id=pk)               # getting perticular instance from model (selecting data)

	form = TaskForm(instance=task)              

	if request.method == 'POST':                           # on updating request (submitting form)
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/tasks')                      # redirect to view tasks

	context = {'form':form}                                # for fill in data in form fields

	return render(request, 'tasks/update_task.html', context)



# handling deleting tasks

def deleteTask(request, pk):
	task = Task.objects.get(id=pk)

	if request.method == 'POST':                 # handling deleteing request
		task.delete()
		return redirect('/tasks')

	context = {'item':task}
	return render(request, 'tasks/delete.html', context)

