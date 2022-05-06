from django.db import models


class News(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    main_photo = models.ImageField(upload_to='news/')
    photo1 = models.ImageField(upload_to='news/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='news/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='news/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='news/', blank=True, null=True)
    photo5 = models.ImageField(upload_to='news/', blank=True, null=True)