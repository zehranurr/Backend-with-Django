from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.contrib.auth.models import User 
from django.forms  import ModelForm,TextInput,Textarea
from django.urls import reverse


# Create your models here.



class Category(MPTTModel):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=10,choices=STATUS)

    slug= models.SlugField(null=False,unique=True)
    parent= TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class MPTTMeta:
        
        order_insertion_by = ['title']


    def __str__(self):
        full_path=[self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k=k.parent
        return '->'.join(full_path[::-1])
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""
    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug':self.slug})
    




class Product(models.Model):
    STATUS=(
        
        ('True','Evet'),
        ('Fasle','Hayır'),
        
        
        
        )
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    keywords = models.CharField(blank=True,max_length=255)
    description = models.CharField(blank=True,max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    price=models.FloatField()
    amount=models.IntegerField()
    detail=RichTextUploadingField()
    slug= models.SlugField(null=False,unique=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""
    def get_absolute_url(self):
        return reverse('product_detail',kwargs={'slug':self.slug})
    

class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image=models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""
    
    
class Comment(models.Model):
    STATUS=(
        ('New','Yeni'),
        ('True','Evet'),
        ('Fasle','Hayır'),
        
        
        
        )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(blank=True,max_length=50)
    comment = models.TextField(blank=True,max_length=200)
    rate=models.IntegerField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.subject
    

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields=['subject','comment','rate']    