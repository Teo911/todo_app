from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect  
from .models import todoModel


# Create your views here.
def ahoj(request):
    all_todo_items = todoModel.objects.all()
    return render(request, 'index.html', {
        'all_items':all_todo_items
    })

def addTodo(request):
    new_item = todoModel(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('todo/')

def deleteTodo(request, todo_id):    
    item_for_deleting = todoModel.objects.get(id=todo_id)
    item_for_deleting.delete()
    return HttpResponseRedirect('todo/')