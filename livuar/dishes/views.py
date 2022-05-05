from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Dish, Category


class MenuView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.prefetch_related('dishes').all()
        return render(request, 'dishes/menu.html', {'categories': categories})