from django.contrib import admin
from .models import School, Player, Bracket, Conference, Calculate_Setting

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'conference', 'wins', 'losses', 'adjEM', 'adjO', 'adjD', 'adjT')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'g', 'gs', 'mp', 'fg', 'fga', 'fg_pct', 'fg2', 'fg2a', 'fg2_pct', 'fg3', 'fg3a', 'fg3_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts')

class BracketAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_name')

class Calculate_SettingAdmin(admin.ModelAdmin):
    list_display = ('avg_adjT', 'avg_adjO', 'hcao', 'hcad')

admin.site.register(School, SchoolAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Bracket, BracketAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Calculate_Setting, Calculate_SettingAdmin)
