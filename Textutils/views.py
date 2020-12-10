
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def analyze(request):
    #get the text
    djtext = request.POST.get('text', "default")
  
    #check checkbox value
    removepunc = request.GET.get("removepunc", "off")
    fullcaps = request.GET.get("fullcaps", "off")
    fullsmall = request.GET.get("fullsmall", "off")
    newlineremover = request.GET.get("newlineremover", "off")
    extraspaceremover = request.GET.get("extraspaceremover", "off")
    charcounter = request.GET.get("charcounter", "off")

    # check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]}{;:'\",<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "Removing Punctuations", "analyzed_text": analyzed}
        djtext = analyzed 

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Changed to Uppercase", "analyzed_text": analyzed}
        djtext = analyzed

    if(fullsmall=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {"purpose": "Changed to lowercase", "analyzed_text": analyzed}
        djtext = analyzed


    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {"purpose": "Remove New Line", "analyzed_text": analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {"purpose": "Remove Extra Space", "analyzed_text": analyzed}
        djtext = analyzed

    if(charcounter == 'on'):
        count = 0
        for char in djtext:
            count += 1
        string = f"Total Character in the given string is {count}"
        params = {"purpose": "Total Character in a string", "analyzed_text": string}
        djtext = analyzed
    return render(request, "analyze.html", params)
        


    

    
    

 