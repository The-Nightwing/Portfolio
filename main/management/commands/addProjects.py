from django.core.management.base import BaseCommand, CommandError
from main.models import Project, WorkExperience
import json

class Command(BaseCommand):
    help = 'Add Projects to the DataBase'

    def handle(self, *args, **options):
        
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

data = {	
    "Own_Projects":[	
        {	
            "Name":"Emojifier",	
            "Description":"Predictig an appropriate emoji on a given user input text.Link to the repository is given below",	
            "Link":"https://github.com/The-Nightwing/Emojifier",	
        },	
        {	
            "Name":"Music Generation",	
            "Description":"Generating new tunes by training 128 songs, using RNN model.",	
            "Link":"https://github.com/The-Nightwing/Music-Generation",	
        },	
        {	
            "Name":"Craigslist-Clone",	
            "Description":"Made a clone of a craigslist-delhi website with better Frontend work than the original website.The data shown is scraped from the https://delhi.craigslist.org/.",	
            "Link":"https://github.com/The-Nightwing/Craigslist-Clone",	
        },	
        {	
            "Name":"Face Recognition",	
            "Description":"Recognizing faces by showing names of the person in front of the webcam.It is implemented using KNN and OpenCV",	
            "Link":"https://github.com/The-Nightwing/Face_Detection"	
        },	
        {	
            "Name":"Portfolio",	
            "Description":"Welcome to my Portfolio. Link to the Project Repository is given below.",	
            "Link":"https://github.com/The-Nightwing/Portfolio"	
        }	
    ],	

    "College_Projects":[	
        {	
            "Name":"Fruket",	
            "Description":"Minor project for DESX101(PIS) course. Made a game using processing and arduino",	
            "Link":"https://github.com/The-Nightwing/Fruket-Game-"	
        },	
        {	
            "Name":"Assembler",	
            "Description":"Converting computer instructions into machine binary codes",	
            "Link":"https://github.com/The-Nightwing/Assembler-12-Bit-In-C-Language-"	
        },	
        {	
            "Name":"Cache Mapping System",	
            "Description":"Implemented three cash mapping techniques in Java.",	
            "Link":"https://github.com/The-Nightwing/Cache-Mapping-Techniques-Java-"	
        },	
        {	
            "Name":"FooCheckr",	
            "Description":"Major project for DESX101(PIS) course. Made a device which detects the condtion of food in a container on the basis of alcohol concentration, humidity , temperature and light intensity.",	
            "Link":"https://github.com/The-Nightwing/FooCheckr"	
        },	
        {	
            "Name":"Color Switch(Game)",	
            "Description":"Color Switch Game implemented in JavaFx, as a Major Project in CSE-201.",	
            "Link":"https://github.com/The-Nightwing/ColorSwitch"	
        },	
        {	
            "Name":"Unix/Linux Shell(in C)",	
            "Description":"Implemented a linux shell in C language with 10 commands. For more information about the project go to the github repository and read out the readme.txt",	
            "Link":"https://github.com/The-Nightwing/Linux-Unix-Shell-in-C"	
        }	
    ]	
}

        