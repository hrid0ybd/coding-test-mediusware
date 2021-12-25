from django.shortcuts import render

# View Frontend


def index(request):
    return render(request, 'build/index.html')
