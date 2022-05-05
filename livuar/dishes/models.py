from django.db import models


class Dish(models.Model):
    ''' Dish model
    '''
    name = models.CharField(max_length=150, unique=True)
    price = models.PositiveIntegerField()
    #ingredients
    category = models.ForeignKey("Category", related_name='dishes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    ''' Ingredient model
    '''
    name = models.CharField(max_length=64)
    dishes = models.ManyToManyField("Dish", related_name='ingredients')

    def __str__(self):
        return self.name


class Category(models.Model):
    ''' Category model
    '''
    name = models.CharField(max_length=64, unique=True)
    big_photo = models.ImageField(upload_to='category/big/')
    small_photo = models.ImageField(upload_to='category/small/')

    def __str__(self):
        return self.name