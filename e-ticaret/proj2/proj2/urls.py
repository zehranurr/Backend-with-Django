import statistics
from django.urls import include, path
from django.conf import settings
from home import views





"""
URL configuration for proj2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from order import views as orderviews

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),

    path('category/<slug>/<int:id>', views.category_products,name='category_products'),
    path('hakkimizda', views.hakkimizda,name='hakkimizda'),
    path('iletisim', views.iletisim,name='iletisim'),
    path('referanslarimiz', views.referanslarimiz,name='referanslarimiz'),
    path('product/<int:id>/<slug>', views.product_detail,name='product_detail'),
    path('search/',views.product_search,name='product_search'),
    path('search_auto/',views.product_search_auto,name='product_search_auto'),
    path('logout/',views.logout_view,name='logout_view'),
    path('login/',views.login_view,name='login_view'  ),
    path('signup/',views.signup_view,name='signup_view'  ),
    path('shopcart/',orderviews.shopcart,name='shopcart' ),
    #path('order_completed/', orderviews.order_completed, name='order_completed'),





    

]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)