from django.urls import path
from . import views

app_name = 'putup'

urlpatterns = [
    path('', views.item, name='item'),
    path('detail/<int:putup_id>/', views.detail, name='detail'),
    path('new/',views.new, name='new'),
]

  # path(URL,関数 or class,name=templateやviewで使うURL名称)