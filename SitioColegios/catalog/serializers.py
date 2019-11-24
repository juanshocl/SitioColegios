from django.contrib.auth.models import User
from catalog.models import School, Ratings, ContactModel, state_province, SchoolType
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = state_province
        fields= ['Id','NameSP']


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    # State_Province = serializers.PrimaryKeyRelatedField( read_only=True)
    # State_Province = StateSerializer(many=True)

    class Meta:
        model = School
        fields = ['Id', 'url','Name', 'Score', 'ImageMD', 'ImageProfile', 'Address','State_Province', 'Phone','Review' ]


    # def create(self, validated_data):

    #     state = state_province(Id=validated_data.get("Id") )
    #     state.save()        
    #     schools = validated_data.get('state_province')
    #     for forSchool in schools:
    #       School.objects.create(State_Provinces=state, **forSchool)
    #     return validated_data

    #  'State_Province'= models.ForeignKey(state_province, on_delete=models.CASCADE) # relacion muchos a uno
    #  = models.CharField(max_length=12)
    # 'Type' = models.ForeignKey(SchoolType, on_delete=models.CASCADE)
    #  = models.TextField(max_length=2000)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactModel
        fields = ['Nombre','Email','Rut','Region','Comuna','Metodo','Newsletter', 'Msg']
