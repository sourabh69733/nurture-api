from django.contrib import admin
from api.models import User, Booking, Advisor

# Register your models here.
admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Advisor)