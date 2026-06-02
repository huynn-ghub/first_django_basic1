from django import template
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader

def index(request):
    data = {
        'title': 'Book List',
    }
    return JsonResponse(data)



def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())