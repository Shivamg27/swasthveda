# Generated by Django 3.1 on 2022-09-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
