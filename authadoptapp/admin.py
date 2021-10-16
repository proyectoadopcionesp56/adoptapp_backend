from django.contrib import admin
from .models.user import User
from .models.pet import Pet
from .models.requestPet import RequestPet

admin.site.register(User)
admin.site.register(Pet)
admin.site.register(RequestPet)