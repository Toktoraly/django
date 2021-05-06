from django.shortcuts import render
from client.models import Client
# from django.http import HttpResponse


# Create your views here.
def client(request):
    clients = Client.objects.all()
    # result =""
    # for cli in client:
    #     result += "{} {} {} {}, ".format(cli.name,cli.surname,cli.age,cli.ilness)
    # return HttpResponse(result)
    return render(request, "client/client.html",{"clients":clients})