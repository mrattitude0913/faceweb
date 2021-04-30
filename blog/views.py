from django.shortcuts import render
from .models import publishedblog,draftblog
from userprofile.models import User_profileing
from django.http import HttpResponse

import base64
from PIL import Image
from io import BytesIO


# Create your views here.
def home(request):
	#print(1)
	u=request.user.username
	usr=User_profileing.objects.get(username=request.user)
	img=usr.image
	return render(request,'dashboard.html',{'name':u,'image':img})


def addblog(request):
	uno=request.user.id
	url=''
	if request.method=='POST':
		ntitle=request.POST['title']
		ncontent=request.POST['content']
		nimage=request.POST['image']
		nbyuser=request.POST['user']
		ndr=request.POST['dd']
		#print(ndraft)
		usr=User_profileing.objects.get(id=nbyuser)
		if ndr=='draft':
			n=draftblog(dtitle=ntitle,dcontent=ncontent,dimage=nimage,dbyuser=usr)
			n.save()
		elif ndr=='publish':
			m=publishedblog(title=ntitle,content=ncontent,image=nimage,byuser=usr)
			m.save()

		return HttpResponse('<script>alert("Blog Saved");window.location="%s"</script>'%url)


	return render(request,'addblog.html',{'id':uno})

def draft(request):
	u=User_profileing.objects.get(username=request.user)
	n=draftblog.objects.filter(dbyuser=u)
	return render(request,'draft.html',{'db':n})

def published(request):
	u=User_profileing.objects.get(username=request.user)
	p=publishedblog.objects.filter(byuser=u)
	return render(request,'published.html',{'pb':p})