from django.contrib import admin
from django.urls import path, include
from allauth.account.views import signup, login, password_change
from Mad_Messenger.views import personal_account_details

urlpatterns = [
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
    path('accounts/account_details/<str:username>/', personal_account_details, name="personal_account_details")
]


