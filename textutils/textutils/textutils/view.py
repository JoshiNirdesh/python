from django.http import HttpResponse
from django.shortcuts import render

def index(request):
 
    return render(request,"index.html")

def analyze(request):
    djtext = request.GET.get("text","default")
    punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzedText = ""
    for char in djtext:
        if char not in punc:
            analyzedText=analyzedText+char
            
    params = {"purpose":"Remove Punchuation","text":analyzedText}

    return render(request,"analyze.html",params)
