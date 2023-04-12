from django.contrib import admin
from .models import Team
from import_export.admin import ImportExportMixin
# Register your models here.

class TeamAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('team', 'school1', 'school2', 'school3')
    list_filter = ['school1', 'school2', 'school3']
    search_fields = ['team', 'email']

admin.site.register(Team, TeamAdmin)
