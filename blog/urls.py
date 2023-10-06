from django.urls import path

from . import views

urlpatterns= [

    path('',views.index,name='starting_page'),
    path('posts',views.posts,name='post_page'),
    path('post/<slug:slug>',views.single_post,name='post_details'),
    path('k',views.karbaran_list),
    path('p',views.product_list,name='product-list'),
    path('<slug:slug>',views.product_details,name='product-detail'),

]