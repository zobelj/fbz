from djongo import models
from django import forms

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
    adjO = models.FloatField(default=0.0)
    adjD = models.FloatField(default=0.0)
    adjT = models.FloatField(default=0.0)

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
    