from django.shortcuts import render
from .models import School, SchoolType, User, Ratings, state_province

# Create your views here.
def index(request):
    promedio_rating= School.average_rating
    colegio= School.objects.get(Id='4ec50c53-669a-4488-b13d-efa15cd80018')
    
    return render(
        request, 'index.html',
        context={'promedio_rating':promedio_rating, 'colegio': colegio},
    )
