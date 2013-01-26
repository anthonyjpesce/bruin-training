from admissions.models import Year
from django.shortcuts import render
from django.db.models import Count, Avg

def index(request):
    context = {
        'years': Year.objects.all(),
    }
    return render(request, 'index.html', context)