# Generated by Django 5.1 on 2024-08-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderForm', '0016_order_area1_order_discount1_order_total_price1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
