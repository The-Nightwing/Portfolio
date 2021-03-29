from django.urls import path
from main import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index, name="index"),
    path('project/',views.projects,name="projects"),
    path('skills/',views.skills,name="skills"),
    path('looc/',views.life,name="life"),
    path('work_experience',views.work_experience,name="wexp"),
    path('resume',views.resume,name="resume")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)