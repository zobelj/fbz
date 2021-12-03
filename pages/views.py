from django.shortcuts import render
from bracket.models import School

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def schools_view(request):
    return render(request, 'schools.html', {'schools': School.objects.all()})

def school_view(request, school_name):
    return render(request, 'schools.html', {'schools': School.objects.filter(name=school_name.replace('-', ' '))})

def conference_view(request, conference_name):
    return render(request, 'schools.html', {'schools': School.objects.filter(conference=conference_name)})
