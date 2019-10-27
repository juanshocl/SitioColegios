from django.shortcuts import render
from .models import School, SchoolType, User, Ratings, state_province

# Create your views here.
def index(request):
    return render(
        request, 'index.html',
        context={},
    )
