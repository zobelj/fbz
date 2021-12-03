from django.contrib import admin
from .models import School, Bracket, Conference, Calculate_Setting

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('_id', 'name', 'rank', 'conference', 'wins', 'losses', 'adjEM', 'adjO', 'adjD', 'adjT')

class BracketAdmin(admin.ModelAdmin):
    list_display = ('_id', 'name', 'description')

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('_id', 'name', 'full_name')

class Calculate_SettingAdmin(admin.ModelAdmin):
    list_display = ('_id', 'avg_adjT', 'avg_adjO', 'hcao', 'hcad')

admin.site.register(Bracket, BracketAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Calculate_Setting, Calculate_SettingAdmin)

