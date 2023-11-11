from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from product.models import CommentForm,Comment
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout



# Create your views here.
def index (request):
    return HttpResponse("product sayfası")



@login_required(login_url='/login')
def addcomment(request,id):
    url=request.META.get('HTTP_REFERER')
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            current_user=request.user


            data =Comment()
            data.user_id=current_user.id
            data.product_id=id
            data.subject=form.cleaned_data['subject']
            data.comment=form.cleaned_data['comment']
            data.rate=form.cleaned_data['rate']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Yorumunuz başarı ile gönderilmiştir.Tesekkür ederiz ")
            
            return HttpResponseRedirect(url)
    messages.error(request,"Yorumunuz kaydedilmedi")    
    return HttpResponseRedirect(url)    
   
