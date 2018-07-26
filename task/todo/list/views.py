from django.shortcuts import render

# Create your views here.
from models import TaskModel
from datetime import datetime

@csrf_exempt
def create_task(request):
    try:
        if request.method=='POST':
            title = request.POST('title')
            description = request.POST.get('description')
            completion_date = datetime.strptime(request.POST[completion_date],%d/%m/%Y %H:%M )
            priority = request.POST['priority']
            TaskModel.objects.create(title=title,description=description,completion_date=completion_date,priority=priority)
    except Exception as e:
        raise e
@csrf_exempt
def edit_task(request,pk=None):
    try:
        if request.method=='POST':
            task = TaskModel.objects.filter(id=pk).first()
            title = request.POST('title')
            description = request.POST.get('description')
            completion_date = datetime.strptime(request.POST[completion_date],%d%m%Y %H:%M)
            task.title = title
            task.description = description
            task.completion_date = completion_date
            task.priority = priority
            task.save()
    except Exception as e:
        raise e
        
@csrf_exempt
def view_incomplete_task(request):
    try:
        if request.method == 'GET':
            incomplete_tasks = TaskModel.objects.filter(is_completed=False)
            incomplete_tasks_list = [dict(title=task.title,
                                          completion_date=task.completion_date.strftime('%d/%m/%Y %H:%M'))
                                     for task in incomplete_tasks]
    except Exception as e:
        raise e    
@csrf_exempt
def delete_task(request, id):
   delpost = TaskModel.objects.get(pk = id)
   delpost.delete()
   

