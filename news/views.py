from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

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
    if request.method == "POST":
        search = request.POST.get('search')
        n_data = News.objects.filter(title__icontains=search)
        paginator = Paginator(n_data, 50)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        data = {
            'newsData': object
        }
        return render(request, 'pages/news.html', data)

    else:
        n_data = News.objects.all()
        paginator = Paginator(n_data, 2)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        data = {
            'newsData': page_obj,
        }
        return render(request, 'pages/news.html', data)