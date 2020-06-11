from django.urls import path
from map import views
urlpatterns=[
    path('getcity/',views.getCity),
    path('getshop/',views.getShop),
    path('getcoffee/',views.getCoffee),
    path("getmore/",views.getMore)
]