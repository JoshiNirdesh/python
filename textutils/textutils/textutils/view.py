from django.http import HttpResponse

def index(request):
    return HttpResponse("Home") 

def rempunc(request):
    return HttpResponse("Remove Punchuation")

def capfirst (request):
    return HttpResponse("Capitalize First")

def newlineremove(request):
    return HttpResponse("New line remove")

def spaceremove (request):
    return HttpResponse("Space remove")

def charcount (request):
    return HttpResponse("Char count")