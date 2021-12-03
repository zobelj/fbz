from django.shortcuts import render, HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bracket.models import School, Conference
from scripts.calculate import calculate

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {'conferences': Conference.objects.all(), 'schools': School.objects.all()})

def about_view(request):
    return render(request, 'about.html', {'conferences': Conference.objects.all()})

def schools_view(request):
    return render(request, 'schools.html', {'schools': School.objects.all(), 'conferences': Conference.objects.all(), 'database_title': 'Schools'})

def school_view(request, school_name):
    school_name = school_name.replace('-', ' ')
    this_school = School.objects.filter(name=school_name)
    return render(request, 'one_school.html', {'schools': this_school, 'conferences': Conference.objects.all(), 'database_title': school_name})

def conference_view(request, conference_name):
    conf_schools = School.objects.filter(conference=conference_name)
    # get the full_name of the conference
    conf_name = Conference.objects.filter(name=conference_name).get().full_name

    return render(request, 'schools.html', {'schools': conf_schools, 'conferences': Conference.objects.all(), 'database_title': conf_name})

@api_view(['GET', 'POST'])
def calculate_view(request):
    # get team names from request
    if request.method == 'POST':
        data = request.data
        team1 = data['team1']
        team2 = data['team2']
        neutral_site = data['neutral_site']

        # calculate the winner
        team1_score, team2_score, team1_prob, team2_prob = calculate(team1, team2, neutral_site)
        res = {
            'team1_score': team1_score,
            'team2_score': team2_score,
            'team1_prob': team1_prob,
            'team2_prob': team2_prob
        }

        return Response(res, status=status.HTTP_200_OK)
    
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def update_database(request):
    if request.user.is_staff:
        from scripts.update_kp_database import update
        print("Updating database...")
        update()
        return HttpResponseRedirect('/')
