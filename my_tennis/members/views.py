from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
from . models import person


# Create your views here.


def hello(request):
    myperson = person.objects.all().values()
    template = loader.get_template('members.html')
    context = {"myperson":myperson}
    return HttpResponse(template.render(context,request))

def details(request , slug):
    myperson = person.objects.get(slug=slug)
    template = loader.get_template('details.html')
    return HttpResponse(template.render({'myperson' : myperson} , request))
    
def main(request):
    myperson = person.objects.all().values()
    template = loader.get_template('main.html')
    context = {'myperson' : myperson}
    return HttpResponse(template.render(context, request))

def testing(request):
    myperson = person.objects.all().order_by( 'lastname',"-id").values() 
    template = loader.get_template('testing.html')
    context = {'myperson': myperson}
    return HttpResponse(template.render(context , request))

def first(request):
    return render(request, 'first.html')

myperson = person.objects.values_list('firstname')
print(myperson)