from django.shortcuts import render
from django.http import HttpResponse
from .models import todoModel


# Create your views here.
def ahoj(request):
    all_todo_items = todoModel.objects.all()
    return render(request, 'index.html', {
        'all_items':all_todo_items
    })