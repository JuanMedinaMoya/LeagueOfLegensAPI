from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages, sessions

from LeagueOfLegends.models import User as Usuario

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repeatpassword = request.POST['repeatpassword']
        lolusername = request.POST['lolusername']
        #user = User.objects.create_user(username=username, password=password)
        #user.save()
        if password == repeatpassword:
            if User.objects.filter(username=username).exists() or username is '':   
                messages.info(request,'Username Taken')
                return redirect('register')
            else:
                userregister = User.objects.create_user(username=username, password=password)
                userregister.save()
                user = Usuario(user=userregister,lolusername=lolusername)
                user.save()
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        #print('User created' + user)
        return redirect('/')

    else:
        return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            #request.session['user'] = user.username

            usuario = Usuario.objects.filter(user=user)
            print(usuario)
            if not usuario:
                usuario = None
            else:
                usuario = usuario[0]
                request.session['lolusername'] = usuario.lolusername
                request.session.modified = True
            

            return  redirect('/')
        else:
            messages.info(request, 'Invalid login')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')