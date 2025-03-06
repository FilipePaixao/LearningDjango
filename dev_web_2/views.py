from django.http import HttpResponse
from django.shortcuts import render

def testRender(request):
    return render(request, 'first.html')