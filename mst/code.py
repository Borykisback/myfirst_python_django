from django.shortcuts import render

def standart(request):
    return render(request, "home.html")
