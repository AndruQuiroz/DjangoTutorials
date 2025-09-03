from django.urls import path
from .views import HomePageView, AboutPageView, ProductIndexView, ProductShowView, ProductCreateView # Modificado

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'), # Añadido
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
]