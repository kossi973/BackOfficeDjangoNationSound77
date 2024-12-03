from django.urls import path
from .views import login_user, logout_user, signup, user_info

urlpatterns = [
    path('user_info/', user_info, name="user_info"),
    path('signup/', signup, name="signup"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
]