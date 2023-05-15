from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Intros

# Create your views here.
def intro(request):
    mymembers = Intros.objects.all().values()
    template = loader.get_template('myfirst.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))

def members(request):
    mymembers = Intros.objects.all().values()
    template = loader.get_template('allmembers.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))
   

def details(request, slug):
    memberDetails = Intros.objects.get(slug = slug)
    template = loader.get_template('details.html')
    context = {

        'memberDetails' : memberDetails
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('test.html')
    context = {
        'fruits' : ['oranges', 'apples', 'pineapples'],
    }
    return HttpResponse(template.render(context, request))