from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":

        a = request.POST.get('input_text')

        new_hello_world = HelloWorld()
        new_hello_world.text = a
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()

        return render(request,'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list' : hello_world_list})

