from django.contrib import admin
from .models import Team
from import_export.admin import ImportExportMixin
from django.contrib.auth import get_user_model

# Register your models here.

# class UcpcAdmin(ImportExportMixin, admin.ModelAdmin):
#         model = UcpcUser
#         list_display = ['email']
#         list_filter = ['email']
#         search_fields = ['email']

class TeamAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('team', 'school1', 'school2', 'school3')
    list_filter = ['school1', 'school2', 'school3']
    search_fields = ['team', 'email']

# admin.site.register(UcpcUser, UcpcAdmin)
admin.site.register(get_user_model())
admin.site.register(Team, TeamAdmin)
