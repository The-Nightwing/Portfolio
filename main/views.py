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
    stats = models.BlogStats.objects.all()

    for stat in stats:
        total_views = stat.total_views
        total_claps = stat.total_claps
        total_fans = stat.total_fans
        total_no_blogs = stat.total_blogs

    context = {
        'views':total_views,
        'claps':total_claps,
        'fans': total_fans,
        'no_blogs':total_no_blogs
    }

    return render(request, 'main/life.html',context)

def work_experience(request):
    we = models.WorkExperience.objects.all();
    context = {
        'work_ex':[]
    }

    for w in we:
        context['work_ex'].append({
        'name' : w.name,
        'position' : w.position,
        'link' : 'https://www'+w.link,
        'description' : w.description,
        'startDate' : w.startDate,
        'endDate' : w.endDate,
        })

    return render(request,'main/work_exp.html',context)