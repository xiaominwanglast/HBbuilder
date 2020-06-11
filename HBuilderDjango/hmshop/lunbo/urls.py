from django.urls import path
from lunbo import views

urlpatterns=[
    path("images/",views.lunbo),
    path("goods/<int:id>",views.goodsList),
    path("getcategory/",views.getCategory),
    path("category/<int:id>", views.categoryId),
    path("getgouwu/<int:id>",views.getgouwu)
]