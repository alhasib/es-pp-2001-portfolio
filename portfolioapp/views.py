from django.shortcuts import render, HttpResponse, redirect
from .models import * 
from portfolioapp.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url = 'login')
def about_me(request,name):
    profile = Profile.objects.get(user__username = name)
    about_me = AboutMe.objects.get(user__username = name)
    context = {'about_me':about_me, 'profile':profile}
    return render(request, 'about_me.html', context)

def skill(request, name):
    profile = Profile.objects.get(user__username = name)
    skills = Skill.objects.filter(user__username = name)
    context = {'skills':skills, 'name':name, 'title':'skills', 'profile':profile}
    return render(request, 'skill.html', context)

def interest(request, name):
    profile = Profile.objects.get(user__username = name)
    interest = Interest.objects.filter(user__username = name)
    context = {'interest':interest, 'name':name, 'title':'interests', 'profile':profile}
    return render(request, 'interest.html', context)

def award(request, name):
    profile = Profile.objects.get(user__username = name)
    award = Award.objects.filter(user__username = name)
    context = {'award':award, 'name':name, 'title':'awards', 'profile':profile}
    return render(request, 'award.html', context)

def education(request, name):
    profile = Profile.objects.get(user__username = name)
    education = Education.objects.filter(user__username = name)
    context = {'education':education, 'name':name, 'title':'education', 'profile':profile}
    return render(request, 'education.html', context)


def experience(request, name):
    profile = Profile.objects.get(user__username = name)
    experience = Experience.objects.filter(user__username = name)
    context = {'experience':experience, 'name':name, 'title':'Experience', 'profile':profile}
    return render(request, 'experience.html', context)

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user:
                login(request, user)
                return redirect('custom-admin')
            else:
                message = "Username or Password is incorrect"
                form = LoginForm()
                context = {'message':message, 'form':form}
                return render(request, 'registration/login.html', c)
    else:
        form = LoginForm()
        context = {'form':form}
        return render(request, 'registration/login.html', context)
    return render(request, 'registration/login.html')

def log_out(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                p_message = "Password Didn't Match"
                form = UserForm()
                context = {'form':form, 'p_message':p_message}
                return render(request, 'registration/signup_form.html', context)
            try:
                user = User.objects.get(username = username)
                if user:

                    message = ' Name Already Exist'
                    form = UserForm()
                    context = {'form':form, 'message':message, 'name':username}
                    return render(request, 'registration/signup_form.html', context)
                else:
                    user = User.objects.create_user(username = username, password = password)
                    return HttpResponse("Registered successfully")
            except:
                pass 
            

    form = UserForm()
    context = {'form':form}
    return render(request, 'registration/signup_form.html', context)



def c_admin(request): 

    return render(request, 'custom_admin.html')

def admin_skills(request):
    try:
        skills = Skill.objects.filter(user__username = request.user)
        if skills:

            context = {'skills':skills}
            return render(request, 'admin_skills.html', context)
        else:
            message = "No Skill Is Available To Show"
            context = {'message':message}
            return render(request, 'admin_skills.html', context)
    except:
        pass

def add_skill(request):
    if request.method == 'POST':
        form = AddSkillForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            context = {'form':form}
            return redirect('admin_skill')
    else:
        form = AddSkillForm()
        context = {'form':form}
        return render(request, 'add_skill.html', context)

