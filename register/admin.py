from django.contrib import admin
from .models import Team, Teammate, Post, Website
from import_export.admin import ImportExportMixin
from django.contrib.auth import get_user_model

# Register your models here.
class TeamAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('ID', 'TeamName', 'FeePayment', 'Rank')
    list_filter = ['Rank', 'FeePayment']
    search_fields = ['TeamName', 'ID']

class TeammateAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('ID', 'Team' ,'Fullname', 'MSSV', 'CMND_CCCD', 'Phone', 'School', 'Leader', 'Occupation', 'JobTitle')
    list_filter = ['Team', 'School', 'Occupation', 'Leader']
    search_fields = ['Team', 'Fullname', 'Phone', 'School', 'MSSV', 'CMND_CCCD', 'JobTitle']
    
class PostAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('ID', 'Date', 'Title', 'Author', 'Thumbnail', 'Post')
    list_filter = ['Date', 'Author']
    search_fields = ['Date', 'Title', 'Author']

class WebsiteAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display=('ID', 'Title', 'Year', 'Deadline', 'Law', 'Award', 'Timeline', 'Organization', 'Sponsor', 'Social')
    list_filter = ['Year', 'Title']
    search_fields = ['Title', 'Year']

admin.site.register(get_user_model())
admin.site.register(Team, TeamAdmin)
admin.site.register(Teammate, TeammateAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Website, WebsiteAdmin)