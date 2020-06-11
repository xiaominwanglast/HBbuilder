from django.urls import path
from portTest import views
urlpatterns=[
    path('showindex',views.showIndex)
]