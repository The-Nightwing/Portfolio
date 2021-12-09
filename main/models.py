from django.db import models

# Create your models here.


class PersonalInfo(models.Model):
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Personal Info'
    
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2056)
    bio = models.CharField(max_length=256)
    img = models.ImageField(upload_to="media/", null=True, verbose_name="")


class Resume(models.Model):
    def __str__(self):
        return "Resume"
    class Meta:
        verbose_name_plural = 'Resume'
    file = models.FileField(upload_to="Resume/", null=True, blank=True)


class BlogStats(models.Model):
    def __str__(self):
        return "Stats"
    class Meta:
        verbose_name_plural = 'MediumStats'

    total_blogs = models.IntegerField(default=0)
    total_views = models.CharField(max_length=2056)
    total_claps = models.CharField(max_length=2056)
    total_fans = models.CharField(max_length=2056)

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
    image_link = models.CharField(max_length=256,default="")