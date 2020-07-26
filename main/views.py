from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def projects(request):
    return render(request, 'main/projects.html')


def skills(request):
    return render(request, 'main/skills.html')

def life(request):
    return render(request, 'main/life.html')
    
def contact(request):
    return render(request, 'main/context.html')
