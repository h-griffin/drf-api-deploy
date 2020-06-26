from django.urls import path
from .views import FlowersList, FlowersDetail

urlpatterns = [
    path('', FlowersList.as_view(), name='flowers_list'),
    path('<int:pk>/', FlowersDetail.as_view(), name='flowers_detail'),
]