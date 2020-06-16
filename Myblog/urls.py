from django.urls import path,include
from . import views

app_name= 'Myblog'
urlpatterns = [
    path('', views.myblog,name='myblog'),
    path('<int:blog_id>', views.detail,name='detail'),
]
