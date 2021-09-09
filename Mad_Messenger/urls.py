from django.contrib import admin
from django.urls import path, include
from allauth.account.views import signup, login, password_change

urlpatterns = [
    path('', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('chat/', include('chat.urls')),
    # Django - Allauth
    path("accounts/signup/", signup, name="account_signup"),
    path("accounts/login/", login, name="account_login"),
    path(
        "accounts/password/change/",
        password_change,
        name="account_change_password",
    ),
]

