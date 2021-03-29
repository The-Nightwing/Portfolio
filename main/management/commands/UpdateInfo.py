from django.core.management.base import BaseCommand, CommandError
from main.models import Project, WorkExperience, PersonalInfo
import json
import datetime 
from django.core.files import File
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Command(BaseCommand):
    help = 'Add Images to DataBase'

    def handle(self, *args, **options):
        p = PersonalInfo(name = 'Shivam Verma',
        description = 'Im a Sophomore at Indraprastha Institute of Information technology, pursuing BTech. in Computer Science and Applied Mathematics. \
         Currently seeking opportunities in the field of Data Science mainly focused on Deep Learning or NLP.',
        
        img = File(os.path.join(BASE_DIR,'media')+'/me.jpg'),
        bio = 'Aspiring Data Scientis',
        )

        p.save()
        