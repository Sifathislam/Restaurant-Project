# Generated by Django 4.2.7 on 2024-01-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_review_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='order.cartitem'),
        ),
    ]
