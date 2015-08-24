from django.shortcuts import render


def index(request):
    context = {}  # So far, we are not specifying any custom context
    return render(request, 'app1/index.html', context)
