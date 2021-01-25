from django.urls import path
from .views import UserListAPIView, UserCreateAPIView, UserDetailAPIView
app_name = "accounts"

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_detail"),
    path("register/", UserCreateAPIView.as_view(), name="user_create"),
    path("<int:id>/", UserDetailAPIView.as_view(), name="user_detail"),
]
#
# urlpatterns = [
#     path('register/', RegisterView.as_view()),
#     path('activate/<str:activation_code>/', ActivateView.as_view()),
#     path('login/', LoginView.as_view()),
#     path('logout/', LogoutView.as_view()),
# ]