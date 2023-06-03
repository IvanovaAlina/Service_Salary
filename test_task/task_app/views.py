from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SalaryForm
from .models import InformSalary, CodeConfirmEmail
from django.http import HttpResponse,Http404
import os
import smtplib
import random
import string
import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def salary_list(request):
    check_code = CodeConfirmEmail.objects.filter(owner = request.user).order_by('-date_added')
    if check_code[0].flag_verify:
        list = InformSalary.objects.filter(owner = request.user).order_by('-date_check')
        context = {'summs': list}
        return render(request, 'salary_list.html', context)
    else:
        return redirect('verify_email')



@login_required
def new_salary(request):
    if request.method != 'POST':
        form = SalaryForm()
    else:
        form =  SalaryForm(data = request.POST)
        if form.is_valid():
            new_salary = form.save(commit=False)
            new_salary.owner = request.user
            new_salary.save()
            return redirect('salary_list')

    context = {"form" : form}
    return render(request, 'new_salary.html', context)

@login_required
def verify_email(request):
    new_code = CodeConfirmEmail.objects.create(owner = request.user,code_verify = "1", email_for_verify = "1", flag_verify = False)
    new_code.save()
    return render(request, 'verify_email.html')


def send_mail_for_verify(request):
    email_str = request.GET["email_acc"] + "@" + request.GET["email_box"]
    if email_str != "":
        smtpObj = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        #smtpObj.starttls()
        loccode = generate_str_for_email(10)
        smtpObj.login('TestForSendEmail@yandex.ru','ncfqoonwmdqgfkvo')
        BODY = "\r\n".join((
                          "From: %s" % "TestForSendEmail@yandex.ru",
                          "To: %s" % email_str,
                          "Subject: %s" % "Verification code" ,
                          "",
                          "Your verification code is: " + loccode
        ))
        new_code = CodeConfirmEmail.objects.create(owner = request.user,code_verify = loccode, email_for_verify = email_str, flag_verify = False)
        new_code.save()
        smtpObj.sendmail("TestForSendEmail@yandex.ru",email_str,BODY) #"Проверочный код для подтверждения входа:"+ generate_str_for_email(10)
        smtpObj.quit()
        return render(request, 'verify_code.html')
    else:
        raise Http404;

def verify_code(request):
    code_get = request.GET["verif_code"]
    try: 
        check_code = CodeConfirmEmail.objects.get(code_verify = code_get, owner = request.user)
        now = datetime.datetime.now(datetime.timezone.utc)
        if check_code.date_added - now > datetime.timedelta(minutes=5): 
            raise Http404
        else:
            check_code.flag_verify = True;
            check_code.save()
    except CodeConfirmEmail.DoesNotExist:
        raise Http404
    return redirect('salary_list')

def generate_str_for_email(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


@login_required
def delete_salary(request, salary_id):
    salary = InformSalary.objects.get(id = salary_id)
    if salary.owner != request.user :
        raise Http404
    if request.method=="POST":
        salary.delete()
        return redirect('salary_list')
    context = {"item":salary}
    return render(request, 'confirm_delete_salary.html', context)
    
