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

class Player(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    g = models.IntegerField()
    gs = models.IntegerField()
    mp = models.FloatField()
    fg = models.FloatField()
    fga = models.FloatField()
    fg_pct = models.FloatField()
    fg2 = models.FloatField()
    fg2a = models.FloatField()
    fg2_pct = models.FloatField()
    fg3 = models.FloatField()
    fg3a = models.FloatField()
    fg3_pct = models.FloatField()
    ft = models.FloatField()
    fta = models.FloatField()
    ft_pct = models.FloatField()
    orb = models.FloatField()
    drb = models.FloatField()
    trb = models.FloatField()
    ast = models.FloatField()
    stl = models.FloatField()
    blk = models.FloatField()
    tov = models.FloatField()
    pf = models.FloatField()
    pts = models.FloatField()

    def as_json(self):
        return dict(
            name=self.name, school=self.school, g=self.g, gs=self.gs, mp=self.mp,
            fg=self.fg, fga=self.fga, fg_pct=self.fg_pct, fg2=self.fg2, fg2a=self.fg2a, fg2_pct=self.fg2_pct,
            fg3=self.fg3, fg3a=self.fg3a, fg3_pct=self.fg3_pct, ft=self.ft, fta=self.fta, ft_pct=self.ft_pct,
            orb=self.orb, drb=self.drb, trb=self.trb, ast=self.ast, stl=self.stl, blk=self.blk, tov=self.tov,
            pf=self.pf, pts=self.pts
        )


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
