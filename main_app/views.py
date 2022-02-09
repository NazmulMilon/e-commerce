from django.shortcuts import render
from .models import Category

# Create your views here.


def home(request):
    return render(request, 'index.html')

# Category
def category_list(request):
    data=Category.objects.all().order_by('-id')
    context={
        'data': data,
    }
    return render(request, 'category_list.html', context)

# Brands
