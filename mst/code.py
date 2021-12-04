from django.shortcuts import render

def standart(request):
    return render(request, "home.html")

def reverse(request):
    user_text = request.GET['usertext']
    revers_text = user_text[::-1]
    number_text = len(user_text.split())
    return render(request, "reverse.html", {'usertext':user_text, 'reversed':revers_text, 'number':number_text})
