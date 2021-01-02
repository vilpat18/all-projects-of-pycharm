"""Banksystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bankapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('branch_info/branch/',views.BranchListAPIView.as_view()),
    path('branch_info/branch/<int:pk>',views.BranchDetailAPIView.as_view()),
    path('bank_info/bank/',views.BankListAPIView.as_view()),
    path('bank_info/bank/<int:pk>',views.BankDetailsAPIView.as_view()),
    path('account_info/account/',views.AccountAPIView.as_view()),
    path('account_info/account/<int:pk>',views.AccountDetailsAPIView.as_view()),
    path('deposit_info/deposit/',views.DepositListAPIView.as_view()),
    path('deposit_info/deposit/<int:pk>',views.DepositDetailsAPIView.as_view()),
    path('withdraw_info/withdraw/',views.WithdrawListAPIView.as_view()),
    path('withdraw_info/withdraw/<int:pk>',views.WithdrawDetailsAPIView.as_view()),
    path('transfer_info/transfer/', views.TransferListAPIView.as_view()),
    path('transfer_info/transfer/<int:pk>', views.TransferDetailsAPIView.as_view()),

]


