# Generated by Django 4.1.5 on 2023-01-12 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(height_field='height', upload_to='', verbose_name='image', width_field='width')),
            ],
        ),
    ]
