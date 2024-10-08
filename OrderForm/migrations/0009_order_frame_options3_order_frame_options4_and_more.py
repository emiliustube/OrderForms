# Generated by Django 5.1 on 2024-08-28 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderForm', '0008_order_frame_options2_order_glass_options2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Frame_Options3',
            field=models.CharField(blank=True, choices=[('NF', 'Nail Fin'), ('SR', 'Stucco/Retro'), ('B', 'Block')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Frame_Options4',
            field=models.CharField(blank=True, choices=[('NF', 'Nail Fin'), ('SR', 'Stucco/Retro'), ('B', 'Block')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Frame_Options5',
            field=models.CharField(blank=True, choices=[('NF', 'Nail Fin'), ('SR', 'Stucco/Retro'), ('B', 'Block')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Glass_Options3',
            field=models.CharField(blank=True, choices=[('LE', 'Low-E'), ('GT', 'Grey Tinted'), ('GR', 'Grey Reflective'), ('B', 'Blue')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Glass_Options4',
            field=models.CharField(blank=True, choices=[('LE', 'Low-E'), ('GT', 'Grey Tinted'), ('GR', 'Grey Reflective'), ('B', 'Blue')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Glass_Options5',
            field=models.CharField(blank=True, choices=[('LE', 'Low-E'), ('GT', 'Grey Tinted'), ('GR', 'Grey Reflective'), ('B', 'Blue')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Grille_Options3',
            field=models.CharField(blank=True, choices=[('no', 'NA'), ('yes', 'YES')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Grille_Options4',
            field=models.CharField(blank=True, choices=[('no', 'NA'), ('yes', 'YES')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Grille_Options5',
            field=models.CharField(blank=True, choices=[('no', 'NA'), ('yes', 'YES')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Size_Options3',
            field=models.CharField(blank=True, choices=[('NES', 'Net/Exact Size'), ('RO', 'Rough Opening')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Size_Options4',
            field=models.CharField(blank=True, choices=[('NES', 'Net/Exact Size'), ('RO', 'Rough Opening')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Size_Options5',
            field=models.CharField(blank=True, choices=[('NES', 'Net/Exact Size'), ('RO', 'Rough Opening')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='bnb3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='bnb4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='bnb5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='color3',
            field=models.CharField(blank=True, choices=[('MB', 'Matt Black'), ('MC', 'Matt Chocolate'), ('MDG', 'Matt Dark Grey'), ('MLG', 'Matt Light Grey'), ('CG', 'Champagne'), ('PW', 'Pure White'), ('YW', 'Yellow Wood'), ('GO', 'Golden Oak'), ('YR', 'Yellow Rosewood'), ('RS', 'Red Sandalwood'), ('C', 'Custom')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='color4',
            field=models.CharField(blank=True, choices=[('MB', 'Matt Black'), ('MC', 'Matt Chocolate'), ('MDG', 'Matt Dark Grey'), ('MLG', 'Matt Light Grey'), ('CG', 'Champagne'), ('PW', 'Pure White'), ('YW', 'Yellow Wood'), ('GO', 'Golden Oak'), ('YR', 'Yellow Rosewood'), ('RS', 'Red Sandalwood'), ('C', 'Custom')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='color5',
            field=models.CharField(blank=True, choices=[('MB', 'Matt Black'), ('MC', 'Matt Chocolate'), ('MDG', 'Matt Dark Grey'), ('MLG', 'Matt Light Grey'), ('CG', 'Champagne'), ('PW', 'Pure White'), ('YW', 'Yellow Wood'), ('GO', 'Golden Oak'), ('YR', 'Yellow Rosewood'), ('RS', 'Red Sandalwood'), ('C', 'Custom')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='height3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='height4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='height5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='lh3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='lh4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='lh5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='notes3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='notes4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='notes5',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='rh3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='rh4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='rh5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='tempgl3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='tempgl4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='tempgl5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='width3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='width4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='width5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='window_type3',
            field=models.CharField(choices=[('none', '-- none --'), ('xo_ox', 'XO or OX - 2 Lite Slider X is Active'), ('xox', 'XOX - 3 Lite Slider X is Active'), ('csmt', 'CSMT - Casement'), ('sh', 'SH - Single Hung'), ('pd', 'PD - Patio Door'), ('dh', 'DH - Double Hung'), ('xx', 'XX - 2 Lite (X Active)'), ('pw', 'PW - Picture Window'), ('awn', 'AWN - Awning'), ('fr', 'FR - Swing Door'), ('bf', 'BF - Bifold Window'), ('tt', 'TT - Tilt and Turn'), ('bw', 'BW - Bay Window')], default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='window_type4',
            field=models.CharField(choices=[('none', '-- none --'), ('xo_ox', 'XO or OX - 2 Lite Slider X is Active'), ('xox', 'XOX - 3 Lite Slider X is Active'), ('csmt', 'CSMT - Casement'), ('sh', 'SH - Single Hung'), ('pd', 'PD - Patio Door'), ('dh', 'DH - Double Hung'), ('xx', 'XX - 2 Lite (X Active)'), ('pw', 'PW - Picture Window'), ('awn', 'AWN - Awning'), ('fr', 'FR - Swing Door'), ('bf', 'BF - Bifold Window'), ('tt', 'TT - Tilt and Turn'), ('bw', 'BW - Bay Window')], default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='window_type5',
            field=models.CharField(choices=[('none', '-- none --'), ('xo_ox', 'XO or OX - 2 Lite Slider X is Active'), ('xox', 'XOX - 3 Lite Slider X is Active'), ('csmt', 'CSMT - Casement'), ('sh', 'SH - Single Hung'), ('pd', 'PD - Patio Door'), ('dh', 'DH - Double Hung'), ('xx', 'XX - 2 Lite (X Active)'), ('pw', 'PW - Picture Window'), ('awn', 'AWN - Awning'), ('fr', 'FR - Swing Door'), ('bf', 'BF - Bifold Window'), ('tt', 'TT - Tilt and Turn'), ('bw', 'BW - Bay Window')], default='none', max_length=50),
        ),
    ]
