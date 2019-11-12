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
    Score = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True) #models.FloatField(null=True, blank=True, default=None)
    ImageMD = models.ImageField(upload_to='static/img//modal')
    ImageProfile = models.ImageField(upload_to='static/img/profile')
    Address = models.CharField(max_length=60)
    State_Province = models.ForeignKey(state_province, on_delete=models.CASCADE) # relacion muchos a uno
    Phone = models.CharField(max_length=12)
    Type = models.ForeignKey(SchoolType, on_delete=models.CASCADE)
    Review = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.Id)

    def score_avg(self):
        mensaje = "Hola que hace"
        # rat = Ratings.objects.filter(Ratings.Schools = self.Id).all()
        return "HOLAAAA" #Ratings.objects.filter(Ratings = self.Id).count()
    
    # def promedio(self):
    #     for item in Ratings:
#######return ', '.join([ Schools.Name for Schools in self.Schools.all()[:3] ])


    #     return rating_prom

    # def average_rating(self):
    #     for item in Ratings:
    #         prom = Ratings.objects.filter(Ratings.Id =  self.Id).aggregate(Avg('Rating'))
    #     return prom
        # for rating in Ratings:
        #     prom = Ratings.objects.filter(rating=Ratings.Id).aggregate(Avg('Rating'))
        # # promedio = Ratings.objects.filter(', '.join([ Schools.Id for Schools in self.Schools.all()[:3] ]). = id).aggregate(Avg('Rating'))
        # return prom.__avg #School.objects.filter(Id=Ratings.Id).aggregate(Avg('Ratings.Rating'))
        # # return self.review_set.aggregate(Avg('Rating'))['rating__avg'] #Promedio de las evaluaciones.
    
    # def get_State(self):
    #     return self.objects.get(Id=Id).
    #     School.objects.get
    #     self.State_Province.description
    # get_State.short_description = 'Nombre Comuna'

class Ratings(models.Model):
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Score = models.IntegerField(choices=RATING)
    Schools = models.ForeignKey(School, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.Id)
    
    def display_School(self):
        return self.Schools.Name
        #', '.join([ Schools.Name for Schools in self.Schools.all()[:3] ])
    display_School.short_description = 'Escuela'

    def get_user(self):
        return self.User.Name+' '+self.User.Last_Name
        #', '.join([ User.Name for User in self.User.all()[:3] ])+' '+ ', '.join([User.Last_Name for User in self.User.all()[:3] ])
    get_user.short_description = 'Usuario'

    def get_email(self):
        return self.User.Email
        #', '.join([ User.Email for User in self.User.all()[:3] ])
    get_email.short_description = 'Email'