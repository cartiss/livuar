from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Dish, Category
from .serializer import DishSerializer, CategorySerializer


class DishView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Dish.objects.prefetch_related('ingredients', 'category').all()
        serializer = DishSerializer(*qs)
        return JsonResponse(serializer.data, status=200)


class CategoryView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Category.objects.prefetch_related('dishes').all()
        serializer = CategorySerializer(*qs)
        return JsonResponse(serializer.data, status=200)