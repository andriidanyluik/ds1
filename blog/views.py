from django.shortcuts import render

def index(request):

    return render(request, 'blog/main/main.html')