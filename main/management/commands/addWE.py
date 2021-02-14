from django.core.management.base import BaseCommand, CommandError
from main.models import Project, WorkExperience
import json
import datetime 

class Command(BaseCommand):
    help = 'Add Projects to the DataBase'

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
    "Name":"Plunes Tech.",
    "Position":"Artifical Intelligence Developer Intern",
    "Description":"Worked towards developing an effective prediction system for creating flexibility in medical services names using NLP.Reduced operation man-hours with web automation to show details of a particular medical service and getting facility details with web scraping techniques.",
    "Link":'plunes.com',
    "startDate":datetime.date(2020,9,7),
    "endDate":datetime.date(2020,12,7)
    },

    {
        "Name":"Opine-IIITD",
        "Position":"Software Maintainer",
        "Description":"Maintaining IIITD's anonymous polling and feedback system by feature additions, fixing bugs, and software upgradations.",
        "Link":"opine.iiitd.edu.in",
        "startDate":datetime.date(2020,10,10),
        "endDate":datetime.now()
    }
]