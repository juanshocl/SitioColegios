from django.contrib.auth.models import User
from catalog.models import School, Ratings, ContactModel, state_province, SchoolType
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = state_province
        fields= ['Id','url','NameSP']


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    #State_Province = serializers.PrimaryKeyRelatedField(many=True, queryset=state_province.objects.all())
    class Meta:
        model = School
        fields = ['Id','url','Name', 'ImageMD', 'ImageProfile', 'Address','State_Province', 'Phone','Type','Review' ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactModel
        fields = ['Nombre','url','Email','Rut','Region','Comuna','Metodo','Newsletter', 'Msg']


class TypeSchoolsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SchoolType
        fields=['Id','url','Description']
