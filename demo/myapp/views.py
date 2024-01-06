from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .form import *
# Create your views here.
# def home(request):
#     return HttpResponse("Hello world!")
#render template with render function pass request argument and name of my template
def home(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/myapp")
        else:
            print(form.errors)
    #if it's a GET request or the form is invalid, render the home page
    tasks = ToDo.objects.all()
    form = ToDoForm()
    context = {'tasks':tasks, 'form': form}
    return render(request, "tasks/list.html", context)


# ham nhan vao request và primary key
def updateTodo(request, pk):
    task = ToDo.objects.get(id=pk)

    form = ToDoForm(instance=task)

    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/myapp/home')

    context = {'form': form}

    return render(request, 'tasks/update_todo.html', context)

def deleteTodo(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/myapp/home')

	context = {'item':item}
	return render(request, 'tasks/delete.html', context)