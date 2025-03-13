from django.http import HttpResponse
from django.shortcuts import render

def testRender(request):
    return render(request, 'first.html')

def pessoas(request):
    pessoas = [{
        "name": "John",
        "age": 30,
        "city": "New York"
    }, {
        "name": "Peter",
        "age": 45,
        "city": "London"
    }, {
        "name": "Sally",
        "age": 25,
        "city": "Paris"
    }]
    return render(request, 'pessoas.html', {'pessoas': pessoas})