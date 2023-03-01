from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_home),
    path('<int:pk>/',views.ProductDetailAPIView.as_view()),
    path('create/',views.ProductCreateAPIView.as_view()),
    
]