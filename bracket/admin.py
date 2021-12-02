from django.contrib import admin
from .models import Bracket

# Register your models here.
class BracketAdmin(admin.ModelAdmin):
    list_display = ('bracket_id', 'name', 'description')

admin.site.register(Bracket, BracketAdmin)
