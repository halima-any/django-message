from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required
def homePage(req):
    return render(req,'homePage.html')

def loginPage(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            login(req,user)
            return redirect('homePage')
        else:
            messages.success(req, "Profile details updated.")
       
          
    return render(req,'loginPage.html')

def signupPage(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        usertype=req.POST.get('usertype')
        password=req.POST.get('password')
        confirm_password=req.POST.get('confirm_password')

        if password == confirm_password:
            user=CustomUser.objects.create_user(
                username=username,
                email=email,
                usertype=usertype,
                password=password,
               
            )
            return redirect('loginPage')
        else:
           
            messages.error(req, "password and confrim_password not matched")
    return render(req,'signupPage.html')

def logoutPage(req):
    logout(req)
    return redirect('loginPage')

def addskillPage(req):
    if req.user.usertype == 'viewer':
        All_skill=INTERMEDIATE_MODEL.objects.all()
        current_user=req.user
        if req.method=='POST':
            skill_id=req.POST.get('skill_id')

            skill_name=req.POST.get('skill_name')
            PROFHECEENCY=req.POST.get('PROFHECEENCY')
            myobj=get_object_or_404(INTERMEDIATE_MODEL,id=skill_id)
            if SKILL_MODEL.objects.filter(user=current_user,skill_name=myobj.skill_name).exists():
                return HttpResponse("skill already exists")
            

            skill=SKILL_MODEL(
                user=current_user,
                skill_name=myobj.skill_name,
                PROFHECEENCY=PROFHECEENCY,

            )
            skill.save()
            text={
                 'All_skill':All_skill
            }

               

            
            return render(req,'addskillPage.html',text)


def addEducation(req):
    if req.user.usertype == 'admin':
        return render(req,'addEducation.html')
    else:
        return HttpResponse('You are not authoirzed to access this page')

def addInterest(req):
    return render(req,'addInterest.html')

def addLanguage(req):
    if req.user.usertype == 'viewer':
        current_user=req.user
        if req.method=='POST':
            RESUME=Language_model(
                user=current_user,
                language_name=req.POST.get('language_name')
            )


        return render(req,'addLanguage.html')
    else:
        return HttpResponse('You are not authoirzed to access this page')

def createResume(req):
    if req.user.usertype == 'viewer':
        current_user=req.user

        if req.method=='POST':
            RESUME=Resume_model(
                user=current_user,
                contact=req.POST.get('contact'),
                designation=req.POST.get('designation'),
                email=req.POST.get('email'),
                age=req.POST.get('age'),
                carrier_summery=req.POST.get('carrier_summery'),
                gender_type=req.POST.get('gender_type'),
                img=req.FILES.get('img'),

            )
            RESUME.save()
            current_user.first_name=req.POST.get('first_name')
            current_user.last_name=req.POST.get('last_name')

            current_user.save()

            messages.success(req, "resume created successfully.")


        return render(req,'createResume.html')
    else:
        return HttpResponse('You are not authoirzed to access this page')
    


def profilePage(req):
    current_user=req.user
    information=get_object_or_404(Resume_model,user=current_user)
    text={
        'information':information
        
    }

    return render(req,'profilePage.html',text)



















    






