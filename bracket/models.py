from djongo import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

REGIONS = (
    ('East', 'East'),
    ('South', 'South'),
    ('West', 'West'),
    ('Midwest', 'Midwest')
)

SEEDS = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
    (13, '13'),
    (14, '14'),
    (15, '15'),
    (16, '16'),
)

# Create your models here.

class School(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    rank = models.IntegerField()
    conference = models.CharField(max_length=100)
    wins = models.IntegerField()
    losses = models.IntegerField()
    adjEM = models.FloatField(default=0.0)
    adjO = models.FloatField(default=0.0)
    adjD = models.FloatField(default=0.0)
    adjT = models.FloatField(default=0.0)

class Conference(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    
class Calculate_Setting(models.Model):
    _id = models.ObjectIdField()
    avg_adjT = models.FloatField(default=0.0)
    avg_adjO = models.FloatField(default=0.0)
    hcao = models.FloatField(default=0.0)
    hcad = models.FloatField(default=0.0)   

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'rank','conference', 'wins', 'losses', 'adjO', 'adjD', 'adjT']

class Bracket(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    schools = models.ArrayField(
        model_container=School,
        model_form_class=SchoolForm,
    )

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
