from django.urls import path

from .views import NewsView, NewsDetailView

urlpatterns = [
    path('news/', NewsView.as_view(), name='news_list'),
    path('news/<slug:news_slug>/', NewsDetailView.as_view(), name='news_details')
]