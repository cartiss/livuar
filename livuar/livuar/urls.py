
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('dishes.urls')),
    path('', include('news.urls')),
    path('', include('reservation.urls')),
    path('', include('main.urls')),
]
