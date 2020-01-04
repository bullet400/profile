from django.urls import path
from products import views

urlpatterns =[
        path('', views.home, name='home'),
        path('create/', views.create, name='create'),
        #path('detail/<int:product_id>/', views.detail, name='detail'),
        path('detail/<int:product_id>/', views.detail, name='detail'),
        path('detail/<int:product_id>/upvotes', views.upvotes, name='upvotes')


]
