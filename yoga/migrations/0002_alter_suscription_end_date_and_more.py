# Generated by Django 4.1.4 on 2022-12-17 07:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscription',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='payment_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]