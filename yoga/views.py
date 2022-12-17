from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
import calendar
from datetime import datetime
from yoga.forms import SuscriptionForm
from yoga.models import Suscription
from django.utils import timezone

def home(request):
    form = SuscriptionForm(request.POST or None)
    if form.is_valid():
        try:
            sus = Suscription.objects.get(user = request.user)
            sus.delete()
        except:
            sus = None
        sform=form.save(commit = False)
        sform.user = request.user
        input_dt = datetime.today()
        res = calendar.monthrange(input_dt.year, input_dt.month)
        last_day = res[1]
        l_date=datetime(input_dt.year,input_dt.month,last_day)
        sform.end_date=l_date

        # sform.save()
        form.save()

    suscribed = False
    try:
        sus = Suscription.objects.get(user = request.user)
    except:
        sus = None

    if sus:
        if sus.end_date > timezone.now().date():
            suscribed = True
    



    if request.user.is_authenticated:
        return render(request, 'users/home.html',{'form':form , 'suscribed':suscribed,'obj':sus})
    else:
        return redirect('login')

