from datetime import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import calendar
from datetime import datetime

# Create your models here.

BATCH_CHOICES = (
    ('6-7AM','6-7AM'),
    ('7-8AM','7-8AM'),
    ('8-9AM','8-9AM'),
    ('5-6PM','5-6PM'),
    
)
class Suscription(models.Model):
    age = models.IntegerField(max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    payment_date = models.DateField(default=timezone.now)
    batch=models.CharField(max_length=6, choices=BATCH_CHOICES, default='6-7AM')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username
