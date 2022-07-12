from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    response = render(request, 'todo_app/index.html')
    return response

@csrf_exempt
def new(request):
    # print('New Page!')

    if request.method == 'GET':
        return render(request, 'todo_app/new.html')

    if request.method == 'POST':
        try:
            body = request.POST
            print('The body is', body)
            print(body['title'], body['description'])
            item = Todo.objects.create(title=body['title'], description=body['description'])
            # return JsonResponse({'success':True})
            return render(request, 'todo_app/view.html', {'success':True, 'item':item})
        except Exception as e:
            print('oops!')
            print(str(e))
            return JsonResponse({'success':False})

def view(request):
    item = {'title': 'Test title', 'description': 'Test description'}
    response = render(request, 'todo_app/view.html', {'item':item})
    return response
    
