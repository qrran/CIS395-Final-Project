from django.contrib import admin

# Register your models here.

from . models import Record, CommunityEngagement

admin.site.register(Record)
admin.site.register(CommunityEngagement)