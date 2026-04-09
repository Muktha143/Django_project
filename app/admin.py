from django.contrib import admin
from .models import Gender, State, Pincode, UserData

# Register your models here.
admin.site.register(UserData)
admin.site.register(Gender)
admin.site.register(State)
admin.site.register(Pincode)