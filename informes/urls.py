from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('create-post/', views.create_post, name='create_post'),
    path('procurar', views.procurar, name='procurar'),
    path('procure', views.procure, name='procure'),
    path('dia', views.dia, name='dia'),
    path('hora', views.hora, name='hora'),
    
  
 
]
