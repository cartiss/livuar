# Generated by Django 4.0.4 on 2022-05-06 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_main_photo_news_photo5_alter_news_photo1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='some-slug'),
            preserve_default=False,
        ),
    ]
