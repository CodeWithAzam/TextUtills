from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext= request.POST.get('text','default')
    
    # Check checkbox values
    
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    
    #Check which checkbox is on
    
    if removepunc=="on":
        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed= ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params= {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed+char
        params = {'purpose': 'Removed Space', 'analyzed_text': analyzed}
    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
    





# Personal Navigator!!!

# def ex1(request):
#     s=Navigation Bar <br> </h2>
#     <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
#     <a href="https://www.facebook.com/"> Facebook </a> <br>
#     <a href="https://www.flipkart.com/"> Flipkart </a> <br>
#     <a href="https://www.hindustantimes.com/"> News </a> <br>
#     <a href="https://www.google.com/"> Google </a> <br>
#     return HttpResponse(s)