from django.urls import path

from . import views

urlpatterns = [
    path('feedback/', views.FeedbackCreateAPIView.as_view()),
]
