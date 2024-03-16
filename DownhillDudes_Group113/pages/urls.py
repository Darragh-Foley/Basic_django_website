from django.urls import path
from . import views

urlpatterns = [
    path('', views.trail_list, name='home'),
    path('trail/<int:trail_id>/', views.trail_detail, name='trail_detail'),
    path('about/', views.about_page, name='about'), 
    path('contact/', views.contact_page, name='contact'),
    path('3/0/8', views.magic_page, name='magic_page'),
    path('admin/', views.admin_page, name='admin_page'), 
]
