from django.shortcuts import render,redirect
from .models import writer
from blogs.models import verified_writer
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
import smtplib 
import os 
import math, random
from django.core.files.storage import FileSystemStorage

writer_created_email=''
writer_created_name=''
writer_created_password=''

@csrf_protect
@csrf_exempt
def login(req):
    req.session.flush()
    req.session['default_mode']='T'
    login_page=loader.get_template('login.html')
    return HttpResponse(login_page.render({}))

@csrf_protect
@csrf_exempt
def validate(req):
    writer_name=req.POST['writer_name']
    writer_password=req.POST['writer_pass']
    w=writer.objects.filter(first_name=writer_name,password=writer_password)
    print(len(w))
    if(len(w)>=1):
        req.session['default_mode']='F'
        query_string='name='+w.values()[0]['first_name']+'&id='+w.values()[0]['writer_id']
        response=redirect('/home?'+query_string,name='aman')
        return response
    else:
        message='INVALID CREDENTIALS!'
        return redirect("/writers/messagedLogin?message="+message)
    
@csrf_protect
@csrf_exempt
def register(req):
    register_page=loader.get_template('register.html')
    return HttpResponse(register_page.render({}))

@csrf_protect
@csrf_exempt
def step1(req):
    writer_email=req.POST['writer_email']
    writer_name=req.POST['writer_name']
    writer_password=req.POST['pass2']
    c_writer_id=writer_name[:3]+writer_password[:3]
    success_page=loader.get_template('registration_success.html')
    pass_register=loader.get_template('password_auth.html')
    if(req.FILES['profile_picture']):
        upload = req.FILES['profile_picture']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
    writer_new=writer(profile_picture=file_url,first_name=writer_name,email=writer_email,password=writer_password,writer_id=c_writer_id)
    
    writer_new.save()
    v=verified_writer(profile_picture=file_url,writer_name=writer_name,writer_id=c_writer_id)
    v.save()
    return HttpResponse(success_page.render({'message':'Registration Success!'}))

@csrf_protect
@csrf_exempt
def step2(req):
    pass1=req.POST['pass1']
    pass2=req.POST['pass2']
    success_page=loader.get_template('registration_success.html')
    pass_register=loader.get_template('password_auth.html')
    if(pass1 == pass2):
        writer_created_password=pass1
        print(writer_created_email)
        writer_new=writer.objects.last()
        writer_new.password=pass2
        writer_new.writer_id=writer_new.first_name[:3]+writer_new.password[:3]
        writer_new.save()
        v=verified_writer(writer_name=writer_new.first_name,writer_id=writer_new.writer_id)
        v.save()
        return HttpResponse(success_page.render({}))
    else:
        return HttpResponse(pass_register.render({'message':"password didn't match. RE-ENTER"}))
    
def success(request):
    success_page=loader.get_template('registration_success.html')
    return HttpResponse(success_page.render({}))
# #automatic mail sender
# smtp = smtplib.SMTP('smtp.gmail.com', 587) 
# smtp.ehlo() 
# smtp.starttls() 
# smtp.login('2022amankumar@gmail.com', 'DoraAman@07') 
# def generate_otp():
#     digits='0123456789'
#     otp=''
#     for i in range(4):
#         otp+=digits[math.floor(random.random()*10)]
#     return otp  

# msg ="Good!", "Hi there! Enter this OTP to enter into the system: " + generate_otp()
   
  
# # smtp.sendmail(from_addr="helloaman404@gmail.com", 
# #               to_addrs=to, msg=msg.as_string()) 

@csrf_protect
@csrf_exempt  
def login_otp(req):
    generate_otp=loader.get_template('generate_otp.html')
    return HttpResponse(generate_otp.render({}))

def normal_login(req):
    req.session.flush()
    req.session['default_mode']='T'
    login_page=loader.get_template('login.html')
    print('here is default')
    return HttpResponse(login_page.render({}))

def messagedLogin(req):
    message=req.GET.get('message')
    loginPage=loader.get_template('messagedLogin.html')
    return HttpResponse(loginPage.render({'message':message}))
    
