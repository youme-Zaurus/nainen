from django.contrib import admin
from .models import RasPi, User, UserBottle, BottleType, Container, ContainerImage

# Register your models here.
# @admin.register(UserBottle)

admin.site.register(RasPi)
admin.site.register(User)
admin.site.register(UserBottle)
admin.site.register(BottleType)
admin.site.register(Container)
admin.site.register(ContainerImage)
