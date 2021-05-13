from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts import views


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # new
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),      # new
    path('api/account/', views.create_account, name='create_user'),
    path('api/user/', views.UserCurrent.as_view(), name='get_user_current'),
    path('api/user/<int:pk>/', views.UserById.as_view(), name='get_user_by_id'),
    path('api/users/', views.get_users, name='get_list_user'),
]
