from django.shortcuts import render
from doctor.models import Doctor
# from django.http import HttpResponse

# Create your views here.
def doctor(request):
    doctors = Doctor.objects.all()
    # results = "<ul>"
    # for doc in doctors:
    #     results += "<li>{} {} {}</li>".format(doc.name,doc.surname,doc.age,)
    #     results +="</ul>"
    # return HttpResponse (results)
    return render(request, "doctor/doctor.html",{"doctors":doctors})

