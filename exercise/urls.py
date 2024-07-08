from django.urls import path
from .views import TrainingList, TrainingDetail

urlpatterns = [
    path('api/trainings/', TrainingList.as_view(), name='training_list'),
    path('api/trainings/<int:pk>/', TrainingDetail.as_view(), name='training_detail'),
]
