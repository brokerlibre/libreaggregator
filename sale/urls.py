from django.urls import path

from . import views

urlpatterns = [
    path('', views.SaleList.as_view()),
    path('<int:pk>/', views.SaleDetail.as_view()),
]
