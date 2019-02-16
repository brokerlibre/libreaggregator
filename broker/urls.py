from django.urls import path

from . import views
                                                                                
urlpatterns = [
    path('', views.BrokerList.as_view()),
    path('<int:pk>/', views.BrokerDetail.as_view()),
]
