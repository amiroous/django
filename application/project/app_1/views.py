from django.shortcuts import render
from project.app_1.models import AccessRecord, Topic, WebPage


def index(request):
    access_records = AccessRecord.objects.order_by('date')
    data = {'access_records': access_records}
    return render(request, 'app_1/index.jinja.html', context=data)

