from django.urls import path
from .import views
urlpatterns=[
path('',views.home,name='home'),
path('productsview/',views.productsview,name='productsview'),
path('aboutview/',views.aboutview,name='aboutview'),
path('blogsview/',views.blogsview,name='blogsview'),
path('contactview/',views.contactview,name='contactview'),
path('loginview/',views.loginview,name='loginview'),
path('registerview/',views.registerview,name='registerview'),
]


