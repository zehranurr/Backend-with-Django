
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate


from home.models import Setting,ContactFormu,ContactFormMessage, UserProfile
from product.models import Product,Category,Images,Comment
from home.forms import SearchForm,SignUpForm
import json
from django.http import JsonResponse

from order.models import ShopCart


def index(request):
    setting=Setting.objects.get(pk=1)
    sliderdata=Product.objects.all()[:4]
    category=Category.objects.all()
    dayproducts=Product.objects.all()[:6]
    lastproducts=Product.objects.all().order_by('-id')[:4]

    randomproducts=Product.objects.all().order_by('?')[:3]
    current_user=request.user
    request.session['cart_items']=ShopCart.objects.filter(user_id=current_user.id).count()            





    context={'setting':setting,'page':'home',
            'sliderdata':sliderdata,
            'dayproducts': dayproducts,
            'lastproduct': lastproducts,
            'randomproducts':randomproducts,
            'category':category}
    return render(request,'index.html',context)


def hakkimizda(request):
    setting=Setting.objects.get(pk=1)
    
    category=Category.objects.all()
    context={'setting':setting,'category':category}
    return render(request,'hakkimizda.html',context)


def iletisim(request):

    if request.method=='POST':
        form=ContactFormu(request.POST)
        if form.is_valid():
            data =ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.subject=form.cleaned_data['subject']
            data.message=form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Mesajınız başarı ile gönderilmiştir")
            return HttpResponseRedirect(reverse('iletisim'))
    setting= Setting.objects.get(pk=1)
    category=Category.objects.all()
    form=ContactFormu()
    context={'setting':setting,'form':form,'category':category}
    return render(request,'iletisim.html',context)    
    


def referanslarimiz(request):
    category=Category.objects.all()
    setting=Setting.objects.get(pk=1)
    context={'setting':setting,'category':category}
    return render(request,'referanslarimiz.html',context)

def product_detail(request,id,slug):
    mesaj="Ürün",id,"/",slug
    product_details=Product.objects.get(pk=id)
    images=Images.objects.filter(product_id=id)
    category=Category.objects.all()
    comments=Comment.objects.filter(product_id=id,status='New')
    context={'category':category,'product_details':product_details,"images":images,'comments':comments}
    return render(request,'product_detail.html',context)


def category_products(request,id,slug):
    products=Product.objects.filter(category_id=id)
    category_data=Category.objects.get(pk=id) 

    category=Category.objects.all()
    context={'products':products,'category':category,'category_data':category_data}
    return render(request,'products.html',context)

def  product_search(request):
    if request.method=='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category=Category.objects.all()
            query =form.cleaned_data['query']
            catid=form.cleaned_data['catid']

            
            if catid==0:
                products=Product.objects.filter(title__icontains=query)
            else:
                products=Product.objects.filter(title__icontainer=query,category_id=catid)
            context={'products':products,
                    'category':category,
                    
                    }
            return render(request,'products_search.html',context)
    return HttpResponseRedirect('/')    


def product_search_auto(request):
    if request.is_ajax():
        q =request.GET.get('term','')
        product=Product.objects.filter(title__icontains=q)
        results=[]

        for rs in product:
            product_json={}
            product_json=rs.title
            results.append(product_json)
        data =json.dumps(results)
    else:
        data='fail'
    mimetype='application/json'
    return HttpResponse(data,mimetype)       



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')  

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')

        else:
            messages.error(request,"Login Hatası !! Kullanıcı adı ya da parola yanlıs")
            return HttpResponseRedirect('/login')



    category=Category.objects.all()
    context={'category':category}
    return render(request,'login.html',context)



def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')

        else:
            messages.error(request,"Login Hatası !! Kullanıcı adı ya da parola yanlıs")
            return HttpResponseRedirect('/login')



    category=Category.objects.all()
    context={'category':category}
    return render(request,'login.html',context)



def signup_view(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)  
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            current_user=request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            messages.success(request,"Hoşgeldiniz...Iyi alisverisler dileriz")
            

            return HttpResponseRedirect('/')
        
    form=SignUpForm()    
    category=Category.objects.all()
    context={'category':category,
                        'form':form,}
    return render(request,'signup.html',context)











# Create your views here.
