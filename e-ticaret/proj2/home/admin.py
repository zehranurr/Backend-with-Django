from django.contrib import admin
from home.models import Setting,ContactFormMessage,UserProfile

# Register your models here.


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','status']
    list_filter=['status']




class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user_name','image_tag','phone','city','country','address']

admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(Setting)
admin.site.register(UserProfile,UserProfileAdmin)