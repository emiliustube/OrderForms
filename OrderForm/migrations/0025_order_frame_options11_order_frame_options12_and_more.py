# Generated by Django 5.1 on 2024-09-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderForm', '0024_delete_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Frame_Options11',
            field=models.CharField(blank=True, choices=[('NF', 'Nail Fin'), ('SR', 'Stucco/Retro'), ('B', 'Block')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Frame_Options12',
            field=models.CharField(blank=True, choices=[('NF', 'Nail Fin'), ('SR', 'Stucco/Retro'), ('B', 'Block')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Glass_Options11',
            field=models.CharField(blank=True, choices=[('LE', 'Low-E'), ('GT', 'Grey Tinted'), ('GR', 'Grey Reflective'), ('B', 'Blue')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Glass_Options12',
            field=models.CharField(blank=True, choices=[('LE', 'Low-E'), ('GT', 'Grey Tinted'), ('GR', 'Grey Reflective'), ('B', 'Blue')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Grille_Options11',
            field=models.CharField(blank=True, choices=[('no', 'NA'), ('yes', 'YES')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Grille_Options12',
            field=models.CharField(blank=True, choices=[('no', 'NA'), ('yes', 'YES')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Size_Options11',
            field=models.CharField(blank=True, choices=[('NES', 'Net/Exact Size'), ('RO', 'Rough Opening')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Size_Options12',
            field=models.CharField(blank=True, choices=[('NES', 'Net/Exact Size'), ('RO', 'Rough Opening')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='bnb11',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='bnb12',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='color11',
            field=models.CharField(blank=True, choices=[('MB', 'Matt Black'), ('MC', 'Matt Chocolate'), ('MDG', 'Matt Dark Grey'), ('MLG', 'Matt Light Grey'), ('CG', 'Champagne'), ('PW', 'Pure White'), ('YW', 'Yellow Wood'), ('GO', 'Golden Oak'), ('YR', 'Yellow Rosewood'), ('RS', 'Red Sandalwood'), ('C', 'Custom')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='color12',
            field=models.CharField(blank=True, choices=[('MB', 'Matt Black'), ('MC', 'Matt Chocolate'), ('MDG', 'Matt Dark Grey'), ('MLG', 'Matt Light Grey'), ('CG', 'Champagne'), ('PW', 'Pure White'), ('YW', 'Yellow Wood'), ('GO', 'Golden Oak'), ('YR', 'Yellow Rosewood'), ('RS', 'Red Sandalwood'), ('C', 'Custom')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='height11',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='height12',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='lh11',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='lh12',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='notes11',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='notes12',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity11',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity12',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='rh11',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='rh12',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='tempgl11',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='tempgl12',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='width11',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='width12',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='window_type11',
            field=models.CharField(choices=[('none', '-- none --'), ('xo_ox', 'XO or OX - 2 Lite Slider X is Active'), ('xox', 'XOX - 3 Lite Slider X is Active'), ('csmt', 'CSMT - Casement'), ('sh', 'SH - Single Hung'), ('pd', 'PD - Patio Door'), ('dh', 'DH - Double Hung'), ('xx', 'XX - 2 Lite (X Active)'), ('pw', 'PW - Picture Window'), ('awn', 'AWN - Awning'), ('fr', 'FR - Swing Door'), ('bf', 'BF - Bifold Window'), ('tt', 'TT - Tilt and Turn'), ('bw', 'BW - Bay Window')], default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='window_type12',
            field=models.CharField(choices=[('none', '-- none --'), ('xo_ox', 'XO or OX - 2 Lite Slider X is Active'), ('xox', 'XOX - 3 Lite Slider X is Active'), ('csmt', 'CSMT - Casement'), ('sh', 'SH - Single Hung'), ('pd', 'PD - Patio Door'), ('dh', 'DH - Double Hung'), ('xx', 'XX - 2 Lite (X Active)'), ('pw', 'PW - Picture Window'), ('awn', 'AWN - Awning'), ('fr', 'FR - Swing Door'), ('bf', 'BF - Bifold Window'), ('tt', 'TT - Tilt and Turn'), ('bw', 'BW - Bay Window')], default='none', max_length=50),
        ),
    ]
