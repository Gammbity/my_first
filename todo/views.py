from django.shortcuts import render, redirect
from .form import CreateTodoModelForm,EditTodoModelForm
from .models import TodoModel
from django.contrib.auth.decorators import login_required


def home_view(request):
    example = 'Abduboriy >>salom '
    return render(request, 'main/home.html', context={
        'example':example
    })

@login_required
def todo_check_view(request, id):
    obj = TodoModel.objects.all().get(id=id)
    if obj.task_status:
        obj.task_status = False
    else:
        obj.task_status = True
    obj.save()
    return redirect('todo_list')    

@login_required
def todo_edit_view(request, id):
    obj = TodoModel.objects.all().filter(id=id)
    if request.method == 'POST':
        form = EditTodoModelForm(data=request.POST)
        if form.is_valid():
            obj.task_name = form.cleaned_data['task_name']
            obj.task_description = form.cleaned_data['task_description']
            obj.save()            
            return redirect('todo_list')
    return render(request, 'main/todo_edit.html', context={
        'tasks': obj
    })    

@login_required
def todo_det_view(request, id):
    obj = TodoModel.objects.all().get(id=id)
    return render(request, 'main/todo_det.html', context={
        'tasks':obj
    })
 
@login_required
def todo_delete_view(request, id):
    TodoModel.objects.all().get(id=id).delete()
    return redirect('todo_list')

@login_required
def todo_list_view(request):
    q = request.GET.get('q', '')
    if request.user.is_authenticated:
        todos = TodoModel.objects.all().filter(user=request.user)
    if q:
        todos = todos.filter(task_name__icontains=q)
    return render(request, 'main/todo_list.html', context={
        "tasks": todos,
        'q': q
    })
    
@login_required
def todo_create_view(request):
    form = CreateTodoModelForm()
    if request.method == 'POST':
        form = CreateTodoModelForm(data=request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('todo_list') 
    return render(request, 'main/todo_create.html', context={
        'create_form':form
    })
