# Generated by Django 3.0.5 on 2022-01-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=1000)),
                ('article_subtitle', models.CharField(max_length=1000)),
                ('article_description', models.TextField(max_length=10000)),
                ('picture_1', models.ImageField(upload_to='')),
                ('picture_2', models.ImageField(upload_to='')),
                ('picture_3', models.ImageField(upload_to='')),
                ('author', models.CharField(max_length=20)),
            ],
        ),
    ]
