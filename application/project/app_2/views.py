from django.shortcuts import render


def index(request):
    data = {
        'header': 'This is Dynamic Message from Data Context to App 2'
    }
    return render(request, 'app_2/index.jinja.html', context=data)
