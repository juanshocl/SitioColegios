from django.contrib import admin

# Register your models here.
from . models import SchoolType, User, state_province, School, Ratings

admin.site.register(SchoolType)
admin.site.register(User)
admin.site.register(state_province)
admin.site.register(School)
admin.site.register(Ratings)