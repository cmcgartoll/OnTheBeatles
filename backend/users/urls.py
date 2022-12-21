from django.urls import path
from .views import LoginView, SignUpView, TokenView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('token/', TokenView.as_view())
]