from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# req -> res
# request handler
# action

def say_hello(request):
    # pull data from database
    # transfrom
    # send email
    return render(request, 'hello.html', {
        'name': 'Mosh',
    })


