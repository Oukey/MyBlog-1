from django.urls import path
from . import views
from django.conf.urls import url
from .views import *


app_name = 'mainapp'


urlpatterns = [
    url(r'^$', index, name='index'),
    # path('blog_list/', blog_list, name='product_list'),
    # path('blog_category/<int:pk>/', blog_category, name='product_category'),
    # path('blog_detail/<int:pk>/', blog_detail, name='product_detail'),
    path('ajax/reload_group/', views.reload_group, name='ajax_reload_group'),  # <-- this one here
    path('ajax/reload_sub_group/', views.reload_sub_group, name='ajax_reload_sub_group'),  # <-- this one here
    # path('page_choice_category/<int:modauto_pk>/<int:pk>/', page_choice_category, name='page_choice_category')

]
