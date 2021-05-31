from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('posts', views.PostList.as_view(), name=views.PostList.name),
    path('register', views.RegisterAPI.as_view(), name=views.RegisterAPI.name),

    path('products/<slug:category_slug>/<slug:product_slug>', views.ProductDetail.as_view(), name=views.ProductDetail.name),
    path('products/<slug:category_slug>',views.CategoryDetail.as_view(), name=views.CategoryDetail.name),
    path('products/search/', views.search),
    path('common-products/', views.CommonProductList.as_view()),
    path('products/',views.ProductsList.as_view(), name=views.ProductsList.name),
    path('categories/', views.CategoryList.as_view(), name=views.CategoryList.name),
    path('api-token', TokenObtainPairView.as_view()),
    path('api-token-refresh', TokenRefreshView.as_view()),
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()), 
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

