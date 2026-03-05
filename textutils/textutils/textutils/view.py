from django.http import HttpResponse
from django.shortcuts import render

def index(request):
 
    return render(request,"index.html")

def analyze(request):
    djtext = request.GET.get("text","default")
    rempun =request.GET.get("rempunc","off")
    fullcap = request.GET.get("fullcap","off")
    newlinerem = request.GET.get("newlinerem","off")
    countchar = request.GET.get("charcount","off")

    if rempun=="on":
        punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzedText = ""
        for char in djtext:
            if char not in punc:
                analyzedText=analyzedText+char
                
        params = {"purpose":"Remove Punchuation","text":analyzedText}
    elif fullcap =="on":
        analyzedText=""
        for char in djtext:
            analyzedText=analyzedText+char.upper()
        params={"purpose":"Full capitalized","text":analyzedText}
    elif newlinerem=="on":
        analyzedText=""
        for char in djtext:
            if char!="\n":
                analyzedText=analyzedText+char
        params={"purpse":"New Line remove","text":analyzedText}
    elif countchar=="on":
        count = 0
        for char in djtext:
            count+=1
        params = {"purpose":"Count Character","text":count}

    return render(request,"analyze.html",params)
