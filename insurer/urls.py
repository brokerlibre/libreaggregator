from django.urls import path

from . import views
                                                                                
urlpatterns = [
    path('', views.InsurerList.as_view()),
    path('<int:pk>/', views.InsurerDetail.as_view()),
]
