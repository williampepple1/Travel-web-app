# Generated by Django 3.0.8 on 2020-09-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20200923_1333'),
        ('Favorite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='favorites', to='Post.Post'),
        ),
    ]
