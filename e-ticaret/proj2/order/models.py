from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm,TextInput
from product.models import Product,User

# Create your models here.
class ShopCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product =models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField()

    def __str__(self):
        return  f"{self.product.title}"
    
    @property
    def amount(self):
        return (self.quantity * self.product.price)
    
    @property
    def price(self):
        return(self.product.price)
    
class ShopCartForm(ModelForm):
    class Meta:
        model=ShopCart
        fields=['quantity']

class Order(models.Model):
    STATUS=(
        
        ('New','New'),
        ('Accepted','Accepted'),
        ('Preparing','Preparing'),
        ('OnShipping','OnShipping'),
        ('Completed','Completed'),
        ('Canceled','Canceled'), 
        
        )        
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    code= models.CharField(editable=False,max_length=5)
    first_name=models.CharField(max_length=18)
    last_name=models.CharField(max_length=10)
    phone=models.CharField(max_length=20,blank=True)
    address=models.CharField(max_length=150,blank=True)
    city=models.CharField(max_length=20,blank=True)
    country=models.CharField(max_length=20,blank=True)
    total=models.FloatField()
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip=models.CharField(max_length=20,blank=True)
    adminnote=models.CharField(max_length=100,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
    
class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=['first_name','last_name','address','phone','city'
                ,'country',] 


class OrderProduct(models.Model):
    STATUS=(
        
        ('New','New'),
        ('Accepted','Accepted'),
        ('Canceled','Canceled'), 
        
        )      
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    amount=models.FloatField()
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product.title


    

    





