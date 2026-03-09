from django.urls import path 
from .views import DetailProductView,CreateProductView,UdapteProductView,DeleteProductView
urlpatterns = [
    path('<int:pk>/',DetailProductView.as_view()),
    path('create/',CreateProductView.as_view()),
    path('<int:pk>/update/',UdapteProductView.as_view()),
    path('<int:pk>/delete/',DeleteProductView.as_view()),

    
]
