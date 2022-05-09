# Generated by Django 4.0.4 on 2022-05-09 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_book_category_alter_grocery_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='products.category'),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grocery', to='products.category'),
        ),
    ]