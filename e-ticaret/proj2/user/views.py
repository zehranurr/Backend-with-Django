
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from product.models import Product,Category
from home.models import UserProfile
from user.forms import ProfilUpdateForm,UserUpdateFrom
from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def index(request):
    category=Category.objects.all()
    current_user=request.user
    profile=UserProfile.objects.get(user_id=current_user.id)

    context={'category':category,'profile':profile}
    return  render(request,'user_profile.html',context)

def user_update(request):
    user_form=UserUpdateFrom(request.POST,instance=request.user)

    profile_form=ProfilUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        messages.success(request,'Your account has been updated!')
        return redirect('/user')
    else:
        category=Category.objects.all()
        user_form=UserUpdateFrom(instance=request.user)
        profile_form=ProfilUpdateForm(instance=request.user.userprofile)
        context={'category':category,'user_form':user_form,'profile_form':profile_form}
    return  render(request,'user_update.html',context)

def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request,'Please correct the error below.<br>'+str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category=Category.objects.all()
        form=PasswordChangeForm(request.user)
        return render(request,'change_password.html',{
            'form':form,'category':category
        })
