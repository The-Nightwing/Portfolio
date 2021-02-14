from django.core.management.base import BaseCommand, CommandError
from main.models import Project, WorkExperience
import json
import datetime 
from django.utils.timezone import now

class Command(BaseCommand):
    help = 'Add Work Experience to the DataBase'

    def handle(self, *args, **options):
        for d in data:
            p = WorkExperience(name = d['Name'],
            position=d['Position'],
            description = d['Description'],
            link = d['Link'],
            startDate = d['startDate'],
            endDate = d['endDate'],
            )
            p.save()


data = [
    {
    "Name":"",
    "Position":"",
    "Description":"",
    "Link":'',
    "startDate":datetime.date(2020,9,7),
    "endDate":datetime.date(2020,12,7)
    },
]