# Generated by Django 3.1.7 on 2022-12-17 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Suscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(max_length=100)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('batch', models.CharField(choices=[('6-7AM', '6-7AM'), ('7-8AM', '7-8AM'), ('8-9AM', '8-9AM'), ('5-6PM', '5-6PM')], default='6-7AM', max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]