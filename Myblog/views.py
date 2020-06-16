from django.shortcuts import render,get_object_or_404
from .models import Myblog

def myblog(request):
    blog=Myblog.objects.all()
    return render(request, 'Myblog/myblog.html',{'blog':blog})

def detail(request,blog_id):
    blog=get_object_or_404(Myblog,pk=blog_id)
    return render(request,'Myblog\detail.html',{'blog':blog})
