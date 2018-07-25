from django.shortcuts import render

# Create your views here.
from models import TaskModel
from datetime import datetime

def create(request):
    try:
        if request.method=='POST':
            title = request.data('title')
            description = request.data.get('description')
            completion_date = datetime.strptime(request.data[completion_date],%d/%m/%y %H:%S )
            TaskModel.objects.create(title=title,description=description,completion_date=completion_date,priority=priority)
    except Exception:
        pass