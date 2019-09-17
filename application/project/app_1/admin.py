from django.contrib import admin
from project.app_1.models import AccessRecord, Topic, WebPage

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
