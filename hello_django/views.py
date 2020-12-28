from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello 世界! ")


def message(request):
    context = {'message': 'Hello 世界! '}
    return render(request, 'message.html', context)


def query(request):
    return render(request, 'query.html')


def query0(request):
    print('executed ', 1)
    print(request.GET)
    print('executed ', 2)
    if request.GET and request.GET.get('q'):
        return HttpResponse(request.GET.get('q'))
    return HttpResponse('empty.')
