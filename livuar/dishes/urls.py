from django.urls import path

from .views import DishView, CategoryView

urlpatterns = [
    path('dishes/', DishView.as_view(), name='dishes'),
    path('categories/', CategoryView.as_view(), name='categories'),
]