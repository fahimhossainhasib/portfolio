from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),  
    path('read_post/<int:post_id>/', views.read_post, name='read_post')
]
