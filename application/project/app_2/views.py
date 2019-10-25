from django.shortcuts import render
from project.app_2.models import User


def index(request):
    users = User.objects.order_by('email')

    data = {
        'users': users
    }

    return render(request, 'app_2/index.jinja.html', context=data)
