from django.shortcuts import render
from .models import School, SchoolType, User, Ratings, state_province

# Create your views here.
def index(request):
    promedio_rating= School.average_rating
    colegio= School.Name
    return render(
        request, 'index.html',
        context={'promedio_rating':promedio_rating, 'colegio': colegio},
    )
