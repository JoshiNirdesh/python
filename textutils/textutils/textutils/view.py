from django.http import HttpResponse
from django.shortcuts import render

def index(request):
 
    return render(request,"index.html")

def rempunc(request):
    text = request.GET.get("text")
    print(text)
    return HttpResponse("Remove Punchuation")

def capfirst (request):
    return HttpResponse("Capitalize First")

def newlineremove(request):
    return HttpResponse("New line remove")

def spaceremove (request):
    return HttpResponse("Space remove")

def charcount (request):
    return HttpResponse("Char count")