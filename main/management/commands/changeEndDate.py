from django.core.management.base import BaseCommand, CommandError
from main.models import Project, WorkExperience
import json
import datetime 
from django.utils import timezone

class Command(BaseCommand):
    help = 'Change end Date of any work Experience'

    def handle(self, *args, **options):
        p = WorkExperience.objects.get(name="")
        p.endDate = timezone.now()
        p.save()