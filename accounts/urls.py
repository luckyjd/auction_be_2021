from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts import views


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # new
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),      # new
    path('api/account/', views.create_account, name='create_user'),
    path('api/user/', views.UserAPIView.as_view(), name='get_user'),
]
