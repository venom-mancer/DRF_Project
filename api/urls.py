from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_home),
    path('<int:pk>/',views.ProductDetailAPIView.as_view()),
    path('create/',views.ProductListCreateAPIView.as_view()),
    path('create/',views.ProductListAPIView.as_view()),
    
]