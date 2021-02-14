from django.shortcuts import render
# Create your views here.
import json
from main import models

def index(request):
    return render(request, 'main/index.html')

def projects(request):
    projects = models.Project.objects.all()
    context={
        'College_Projects':[],
        'Own_Projects':[],
    }
    for p in projects:
        if p.project_type=='College':
            context['College_Projects'].append({
                'Name':p.project_name,
                'Description':p.description,
                'Link':p.github_link
            })
        elif p.project_type=='Own':
            context['Own_Projects'].append({
                'Name':p.project_name,
                'Description':p.description,
                'Link':p.github_link
            })
    return render(request, 'main/projects.html',context)

def skills(request):
    return render(request, 'main/skills.html')

def life(request):
    return render(request, 'main/life.html')

def work_experience(request):
    return render(request,'main/work_exp.html')
