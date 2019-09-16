from django.shortcuts import render


def index(request):
    data = {
        'header': 'This is Dynamic Message from Data Context to App 1'
    }
    return render(request, 'app_1/index.jinja.html', context=data)
