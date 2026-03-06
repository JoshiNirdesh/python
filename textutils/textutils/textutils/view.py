from django.http import HttpResponse
from django.shortcuts import render

def index(request):
 
    return render(request,"index.html")

def analyze(request):
    djtext = request.POST.get("text","default")
    rempun =request.POST.get("rempunc","off")
    fullcap = request.POST.get("fullcap","off")
    newlinerem = request.POST.get("newlinerem","off")
    countchar = request.POST.get("charcount","off")

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
    else:
        return HttpResponse("Error")

    return render(request,"analyze.html",params)
