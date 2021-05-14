from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

    # return HttpResponse("Home")


def analyze(request):
    djtext = request.POST.get('text', 'default')
    purpose_text = ''
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{;}:'"\,=<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        # params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        purpose_text += 'Removed Punctuations, '
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        # params = {'purpose':'All in Upper Case', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        purpose_text += 'All in Upper Case, '
        djtext = analyzed

    if lowercase == "on":
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.lower()
        # params = {'purpose':'All in lower case', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        purpose_text += 'All in lower case, '
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        # params = {'purpose': 'Removed extra spaces', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        purpose_text += 'Removed extra spaces, '
        djtext = analyzed

    if charcounter == "on":
        newtext = ''
        for char in djtext:
            if char != ' ':
                newtext += char

        analyzed = len(newtext)
        purpose_text += 'Counted number of charachters, '

    params = {'purpose': purpose_text, 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
