from rest_framework import serializers

from .models import Dish, Ingredient, Category


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'big_photo', 'small_photo']
        read_only_fields = ['big_photo', 'small_photo']


class DishSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Dish
        fields = ['name', 'price', 'ingredients', 'category']
