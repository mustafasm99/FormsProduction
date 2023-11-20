from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse
from .models import *
from form.models import DataBase , Value_Data


def allTeacher(e):
    if 'user_data' in e.session and 'user_last_form' in e.session:
        form = Form.objects.filter(name__contains = e.session['user_last_form']).first()
        data = filters.objects.filter(form = form).all()
        user_data   = e.session['user_data']
        user_forms  = e.session['user_forms']
    else :
        return redirect('form:home')
    if e.method == 'POST':
        cources = Cource.objects.filter(id__in = e.POST.getlist('course')).all()
        print(cources)
        db = DataBase.objects.filter(UUid = user_data).first()
        Value_Data.objects.create(
            value       = [str(i.name) for i in cources],
            fiald       = "Courses",
            DataBase    = db
        )
        return redirect("form:home")
    print(data)
    return render(e,"student/cources.html",{"data":data})