from django.db import models

# Create your models here.

class Project(models.Model):
    def __str__(self):
        return self.project_name
    
    class Meta:
        verbose_name_plural = 'Projects'

    choices=(
        ('College','College'),
        ('Own','Own')
    )

    project_name = models.CharField(max_length=256)
    project_type = models.CharField(max_length=10,choices=choices,default='College')
    description = models.CharField(max_length=10056)
    github_link = models.CharField(max_length=1024)

class WorkExperience(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Work Experience'
        
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    link = models.CharField(max_length=256,default="")
    description = models.CharField(max_length=10056)
    startDate = models.DateField()
    endDate = models.DateField()