from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    data={
        'categoryData': Category.objects.all(),
        'newsData': News.objects.all(),
    }
    return render(request, 'pages/index.html',data)

def news_details(request, slug):
    find_data = News.objects.get(slug=slug)
    cat_id = find_data.category_id
    related_news = News.objects.filter(category_id=cat_id).exclude(slug=slug)
    data = {
        'newsData':find_data,
        'relatedNews':related_news,
    }
    return render(request, 'pages/news-details.html', data)

def sports(request):
    data={
        'sports':News.objects.all().filter(category=2)
    }
    return render(request,'pages/sports.html',data)

def news(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        data={
            'newsData':News.objects.filter(title__icontains=search)
        }
        return render(request,'pages/news.html',data)
    else:
        data={
        'newsData':News.objects.all()
        }   
        return render(request,'pages/news.html',data)