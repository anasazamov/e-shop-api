from django.urls import path
from .views import ProductView

urlpatterns = [
    path('task', ProductView.as_view()),
    path('task/<int:pk>/', ProductView.as_view()),
]