from django.http import HttpResponse

def index(request):
    return HttpResponse('''<a href="https://www.youtube.com/watch?v=ES-bdt0KUZg&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=8" >Code with harry </a>''')

def about (request):
    return HttpResponse("About Us")