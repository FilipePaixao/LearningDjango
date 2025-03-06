from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello, Django!')

def hello2 (request): 
    return HttpResponse('Hello, Django! 2')