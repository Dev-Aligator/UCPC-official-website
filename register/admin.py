from django.contrib import admin
from .models import Team, Teammate, Post, Website
from import_export.admin import ImportExportMixin
# Register your models here.

class TeamAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('ID', 'TeamName', 'Email', 'FeePayment', 'Rank')
    list_filter = ['Rank', 'FeePayment']
    search_fields = ['TeamName', 'Email', 'ID']

class TeammateAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('ID', 'Team' ,'Fullname', 'MSSV_CMND', 'Phone', 'School', 'Leader', 'Occupation')
    list_filter = ['Team', 'School', 'Occupation', 'Leader']
    search_fields = ['Team', 'Fullname', 'Phone', 'School', 'MSSV_CMND']
    
class PostAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('ID', 'Date', 'Title', 'Author', 'Thumbnail', 'Post')
    list_filter = ['Date', 'Author']
    search_fields = ['Date', 'Title', 'Author']

class WebsiteAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display=('ID', 'Title', 'Year', 'Deadline', 'Law', 'Award', 'Timeline', 'Organization', 'Sponsor', 'Social')
    list_filter = ['Year', 'Title']
    search_fields = ['Title', 'Year']

admin.site.register(Team, TeamAdmin)
admin.site.register(Teammate, TeammateAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Website, WebsiteAdmin)