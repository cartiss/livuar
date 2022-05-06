from django.shortcuts import render
from rest_framework.views import APIView

from .models import News


class NewsView(APIView):
    def get(self, request, *args, **kwargs):
        news = News.objects.all()
        return render(request, 'news/news.html', {'news_list': news})


class NewsDetailView(APIView):
    def get(self, request, news_slug, format=None):
        news = News.objects.get(slug=news_slug)
        return render(request, 'news/newsdetails.html', {'news': news})

