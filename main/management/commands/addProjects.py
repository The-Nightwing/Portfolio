from django.core.management.base import BaseCommand, CommandError
from main.models import Project, WorkExperience
import json

class Command(BaseCommand):
    help = 'Add Projects to the DataBase'

    def handle(self, *args, **options):
        with open('database.json') as f:
            data = json.load(f)
        
        for projects in data['College_Projects']:
            Name = projects['Name']
            Description = projects['Description']
            Link = projects['Link']

            p = Project(project_name=Name,description=Description,project_type='College',github_link=Link)
            p.save()

        for projects in data['Own_Projects']:
            Name = projects['Name']
            Description = projects['Description']
            Link = projects['Link']
            p = Project(project_name=Name,description=Description,project_type='Own',github_link=Link)            
            p.save()
        
        
