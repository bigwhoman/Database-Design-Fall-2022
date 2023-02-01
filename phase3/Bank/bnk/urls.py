from django.urls import path

from bnk.views import (
    login_bankuser, logout_bankuser, register_employee,
    EditCustomerView, get_contracts, give_safebox_to_customer,
    get_safeboxes, cancel_contract
)

app_name = "bnk"

urlpatterns = [
    path("employee/register/", register_employee, name="register_employee"),
    path("login/", login_bankuser, name="login_bankuser"),
    path("logout/", logout_bankuser, name="logout_bankuser"),
    path("customer/", EditCustomerView.as_view(), name="edit_customer_view"),
    path("safebox/give/", give_safebox_to_customer, name="give_safe_box"),
    path("contracts/", get_contracts, name="get_contracts"),
    path("safebox/", get_safeboxes, name="get_safeboxes"),
    path("contracts/delete/", cancel_contract, name="cancel_contract"),
]