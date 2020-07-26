from django.urls import path
from main import views

urlpatterns = [
    path('',views.index, name="index"),
    path('project/',views.projects,name="projects"),
    path('skills/',views.skills,name="skills"),
    path('looc/',views.life,name="life"),
    path('contact/',views.contact,name="contact")
]