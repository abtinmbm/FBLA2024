# Generated by Django 5.0.2 on 2024-02-24 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerprofile',
            name='contact_phone',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='partnerprofile',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('suspended', 'Suspended'), ('active', 'Active')], default='pending', max_length=255),
        ),
        migrations.AlterField(
            model_name='partnerprofile',
            name='website',
            field=models.URLField(),
        ),
    ]