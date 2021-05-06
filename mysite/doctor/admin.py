from django.contrib import admin
from doctor.models import Doctor
from client.models import Client
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Client)