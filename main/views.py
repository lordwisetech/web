from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Todo


# Create your views here.
class showtodo(ListView):
    model = Todo
    template_name = "main/template/list.html"


def create(request):
    if request.method == "POST":
        todo = request.POST['todo']
        new_todo = Todo(todo= todo)
        new_todo.save()
        return redirect('home')
    return render(request, "main/template/index.html")

def delete(request, pk):
    delete = Todo.objects.get(id=pk)
    delete.delete()
    return redirect('home')


def edit(request,pk):
    post = Todo.objects.get(id=pk)
    if request.method == 'POST':
        post.Todo = request.POST['todo']
        post.save()
        return redirect("home")
    context = {'post': post}
    return render(request,"main/template/edit.html",context)