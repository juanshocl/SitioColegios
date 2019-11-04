from django.contrib import admin

# Register your models here.
from . models import SchoolType, User, state_province, School, Ratings

# admin.site.register(SchoolType)
#admin.site.register(User)
#admin.site.register(state_province)
# admin.site.register(School)
#admin.site.register(Ratings)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('Name', 'RatingShool', 'Address', 'get_name', 'Phone', 'get_typeName')
   
    def get_name(self, obj):
        return obj.State_Province.NameSP
    get_name.short_description = 'Comuna'

    def get_typeName(self, obj):
        return obj.Type.Description
    get_typeName.short_description = 'Tipo Establecimiento'

admin.site.register(School, SchoolAdmin)

class SchoolTypeAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Description')

admin.site.register(SchoolType, SchoolTypeAdmin)

class StateProviceAdmin(admin.ModelAdmin):
    list_display = ('Id', 'get_name')
    
    def get_name(self, obj):
        return obj.NameSP
    get_name.short_description = 'Nombre Comuna'


admin.site.register(state_province, StateProviceAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('get_name','Email', 'Phone')

    def get_name(self, obj):
        return(obj.Name+' '+obj.Last_Name)

    get_name.short_description = 'Nombre'

admin.site.register(User, UserAdmin)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('get_email','get_user','Rating')
    
    def get_user(self, obj):
        return obj.User.Name+' '+obj.User.Last_Name
    get_user.short_description = 'Usuario'
    
    def get_email(self, obj):
        return obj.User.Email
    get_email.short_description = 'Email'

    # def get_School(self, obj):

    #    return Ratings.objects.filter(Id='d1b6a49a-dab5-4c12-baad-798799dcd499').Schools.Id

       # return obj.Schools.get(Id='d1b6a49a-dab5-4c12-baad-798799dcd499').Name
        # obj.Schools.get(Id=obj.User).Name
   # get_School.short_description = 'Escuela'

admin.site.register(Ratings, RatingAdmin)