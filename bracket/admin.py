from django.contrib import admin
from .models import School, Bracket

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('_id', 'name', 'rank', 'conference', 'wins', 'losses', 'adjO', 'adjD', 'adjT')

class BracketAdmin(admin.ModelAdmin):
    list_display = ('_id', 'name', 'description')

admin.site.register(Bracket, BracketAdmin)
admin.site.register(School, SchoolAdmin)
