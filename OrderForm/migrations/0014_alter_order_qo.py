# Generated by Django 5.1 on 2024-08-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderForm', '0013_alter_order_notes1_alter_order_notes2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='QO',
            field=models.CharField(choices=[('quote', 'Quote'), ('order', 'Order')], default='none', max_length=50, null=True),
        ),
    ]
