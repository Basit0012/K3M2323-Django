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
]