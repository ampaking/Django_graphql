# Generated by Django 4.0.4 on 2022-05-09 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_book_category_alter_grocery_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
    ]
