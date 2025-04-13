from django.urls import path  # type: ignore
from .views import AccountUserRegisterView, AccountUserLoginView, AccountUserLogoutView

urlpatterns = [
    path('register/', AccountUserRegisterView.as_view(),
         name='account-user-create'),
    path('login/', AccountUserLoginView.as_view(), name='account-user-login'),
    path('logout/', AccountUserLogoutView.as_view(), name='account-user-logout'),
]
