from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bracket.models import School, Conference
from scripts.calculate import calculate
from bracket.models import RegistrationForm

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

    return render(request, 'conference.html', {'schools': conf_schools, 'conferences': Conference.objects.all(), 'database_title': conf_name})

@api_view(['GET', 'POST'])
def calculate_view(request):
    # get team names from request
    if request.method == 'POST':
        data = request.data
        away = data['away']
        home = data['home']
        neutral_site = data['neutral_site']

        # calculate the winner
        away_score, home_score, away_prob, home_prob, total_points, home_spread = calculate(away, home, neutral_site)
        
        res = {
            'away_score': away_score,
            'home_score': home_score,
            'away_prob': away_prob,
            'home_prob': home_prob,
            'total_points': total_points,
            'home_spread': home_spread
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

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return HttpResponseRedirect('/')

    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
