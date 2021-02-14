from django.db import models

# Create your models here.

class Project(models.Model):
    def __str__(self):
        return "Projects"
    project_name = models.CharField(max_length=256)
    description = models.CharField(max_length=10056)
    github_link = models.CharField(max_length=1024)

class WorkExperience(models.Model):
    def __str__(self):
        return "Work Experience"
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    description = models.CharField(max_length=10056)
    startDate = models.DateField()
    endDate = models.DateField()