from django.urls import path

from bnk.views import (
    login_bankuser, logout_bankuser, register_employee,
    EditCustomerView
)

app_name = "bnk"

urlpatterns = [
    path("employee/register/", register_employee, name="register_employee"),
    path("login/", login_bankuser, name="login_bankuser"),
    path("logout/", logout_bankuser, name="logout_bankuser"),
    path("customer/", EditCustomerView.as_view(), name="edit_customer_view"), 
]