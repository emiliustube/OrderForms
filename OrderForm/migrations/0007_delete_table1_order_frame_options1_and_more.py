# Generated by Django 5.1 on 2024-08-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderForm', '0006_table1_remove_order_frame_options1_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Table1',
        ),
        migrations.AddField(
            model_name='order',
            name='Frame_Options1',
            field=models.CharField(blank=True, choices=[('NF', 'Nail Fin'), ('SR', 'Stucco/Retro'), ('B', 'Block')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Glass_Options1',
            field=models.CharField(blank=True, choices=[('LE', 'Low-E'), ('GT', 'Grey Tinted'), ('GR', 'Grey Reflective'), ('B', 'Blue')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Grille_Options1',
            field=models.CharField(blank=True, choices=[('no', 'NA'), ('yes', 'YES')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Size_Options1',
            field=models.CharField(blank=True, choices=[('NES', 'Net/Exact Size'), ('RO', 'Rough Opening')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='bnb1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='color1',
            field=models.CharField(blank=True, choices=[('MB', 'Matt Black'), ('MC', 'Matt Chocolate'), ('MDG', 'Matt Dark Grey'), ('MLG', 'Matt Light Grey'), ('CG', 'Champagne'), ('PW', 'Pure White'), ('YW', 'Yellow Wood'), ('GO', 'Golden Oak'), ('YR', 'Yellow Rosewood'), ('RS', 'Red Sandalwood'), ('C', 'Custom')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='height1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='lh1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='notes1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='rh1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='tempgl1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='width1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='window_type1',
            field=models.CharField(choices=[('none', '-- none --'), ('xo_ox', 'XO or OX - 2 Lite Slider X is Active'), ('xox', 'XOX - 3 Lite Slider X is Active'), ('csmt', 'CSMT - Casement'), ('sh', 'SH - Single Hung'), ('pd', 'PD - Patio Door'), ('dh', 'DH - Double Hung'), ('xx', 'XX - 2 Lite (X Active)'), ('pw', 'PW - Picture Window'), ('awn', 'AWN - Awning'), ('fr', 'FR - Swing Door'), ('bf', 'BF - Bifold Window'), ('tt', 'TT - Tilt and Turn'), ('bw', 'BW - Bay Window')], default='none', max_length=50),
        ),
    ]
