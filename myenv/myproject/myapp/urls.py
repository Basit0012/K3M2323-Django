from django.urls import path, re_path
from . import views 

urlpatterns = [
    path('', views.newmessage, name='newmessage'),
    path('program/', views.program, name='program'),
    path('result/', views.performance, name='performance'),
    path('simplehtml/', views.simplehtml, name='simplehtml'),
    path('grade/',views.grade,name='grade'),
    path('table/',views.table,name='table'),
    path('products',views.products),
    path('prodinfo/', views.prodinfo),
    path('prodsinfo/',views.prodsinfo),
    path('greetings/<str:name>', views.greetings),
    path('foodlist/<str:foodvalue>',views.foodlist),
    path('search/',views.searchquery),
    # Matches URLs like /customer/Alice/ or /customer/Bob/
    re_path(r'^customer/(?P<customername>[a-zA-Z0-9 \w \s]+)/$', views.customer_profile), 
    re_path(r'^customer1/(?P<customername>[\w \s]*)/?$', views.customer_profile1), 
    # + -> compulsory parameter
    # * -> Optional parameter 
    re_path(r'^dob/(?P<date>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})',views.dobdisplay), 
    # \d -> digits with spaces \s
]