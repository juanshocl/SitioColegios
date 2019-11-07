import uuid
from django.db import models
from django.db.models import Avg

# Create your models here.

class SchoolType(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Description = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Id)

class User(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Email = models.CharField(max_length=45)
    Phone = models.CharField(max_length=12)
    Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.Id)

class state_province(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    NameSP = models.CharField(max_length=25)
    
    def __str__(self):
        return str(self.Id)      

class School(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=40)
    RatingShool = models.FloatField(null=True, blank=True, default=None) #models.FloatField(null=True, blank=True, default=None)
    ImageMD = models.ImageField(upload_to='static/img//modal')
    ImageProfile = models.ImageField(upload_to='static/img/profile')
    Address = models.CharField(max_length=60)
    State_Province = models.ForeignKey(state_province, on_delete=models.CASCADE) # relacion muchos a uno
    Phone = models.CharField(max_length=12)
    Type = models.ForeignKey(SchoolType, on_delete=models.CASCADE)
    ShortReview = models.TextField(null=True, blank=True, default=None, max_length=1000)
    Review = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.Id)
    
    def average_rating(self):
        return self.review_set.aggregate(Avg('Rating'))['rating__avg'] #Promedio de las evaluaciones.
    
    
    
    # def get_State(self):
    #     return self.objects.get(Id=Id).
    #     School.objects.get
    #     self.State_Province.description
    # get_State.short_description = 'Nombre Comuna'
    
    # def get_State(self):
    #     return self.State_Province.Description
    # get_State.short_description = 'Comuna'

    def get_typeName(self):
        return ', '.join([ Type.Description for Typedescription in self.Type.all()[:3] ])
    get_typeName.short_description = 'Tipo Establecimiento'

class Ratings(models.Model):
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User = models.ManyToManyField(User)
    Rating = models.IntegerField(choices=RATING)
    Schools = models.ManyToManyField(School)

    def __str__(self):
        return str(self.Id)
    
    def display_School(self):
        return ', '.join([ Schools.Name for Schools in self.Schools.all()[:3] ])
    display_School.short_description = 'Escuela'

    def get_user(self):
        return ', '.join([ User.Name for User in self.User.all()[:3] ])+' '+ ', '.join([User.Last_Name for User in self.User.all()[:3] ])
    get_user.short_description = 'Usuario'

    def get_email(self):
        return ', '.join([ User.Email for User in self.User.all()[:3] ])
    get_user.short_description = 'Email'