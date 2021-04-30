from django.shortcuts import render, redirect
from .models import User_profileing
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from binascii import a2b_base64
import base64
from PIL import Image
import numpy as np
import io



# Create your views here.



def home(request):
	return render(request, 'index.html')

def signup_call(request):
	if request.method=='POST':
		email=request.POST['email']
		uname=request.POST['username']
		passwd=request.POST['password']
		c_passwd=request.POST['c_password']
		img=request.POST['userimage']
		
		#print(imgg)
		i = base64.b64decode(img[22:])
		image = Image.open(io.BytesIO(i))
		imarr = np.array(image)
		#print(imarr)

		url=''
		try:

			u=User_profileing(email=email,username=uname,
				password=passwd,c_password=c_passwd,image=img)
			u.save()
			newuser =User(email=email,username=uname,password=make_password(passwd))
			newuser.save()
			
			return redirect('/user/login/')
		except:
			return HttpResponse('<script>alert("Username already exists..");window.location="%s"</script>'%url)
        
		return redirect('/user/signup/')
	return render(request,'signup.html')
def login_call(request):
	if request.method=='POST':
		uname=request.POST['username']
		passwd=request.POST['password']
		url=''
		try:
			selUser = authenticate(username=uname, password=passwd)
			#print(selUser)
			if selUser:
				#print('came')
				login(request,selUser)
				#print(5)
				return redirect('/blog/dashboard')
		except:
			return HttpResponse('<script>alert("wrong password or username");window.location="%s"</script>'%url)

		
		
	return render(request, 'login.html')
	
def logout_call(request):
	logout(request)
	return redirect('/user/login/')