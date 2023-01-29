import json
from http import HTTPStatus

from bnk.models import BankUser

from django.shortcuts import render
from django.forms.models import model_to_dict
from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
require_http_methods(["GET"])
def get_safeboxes(request):
    ...

require_http_methods(["GET"])
def get_contracts(request):
    ...

require_http_methods(["POST"])
def cancel_contract(request):
    ...

require_http_methods(["POST"])
def give_safebox_to_customer(request):
    ...
class EditCustomerView(View):
    def post(self, request):
        ...
    
    def patch(self, request):
        ...
    
    def delete(self, request):
        ...

require_http_methods(["POST"])
def register_employee(request):
    try:
        json_body = json.loads(request.body)        
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "body must be in json format"},
            status=HTTPStatus.BAD_REQUEST
        )
    
    try:
        username, password = json_body["username"], json_body["password"]
    except KeyError:
        return JsonResponse(
            {"error": "username and password must be provided"},
            status=HTTPStatus.BAD_REQUEST
        )
    
    user = BankUser(username=username, is_staff=True)
    user.set_password(password)
    user.save()
    return JsonResponse(
        {model_to_dict(user, exclude=["password", "email"])}, status=HTTPStatus.CREATED
    )


require_http_methods(["POST"])
@login_required
def logout_employee(request):
    logout(request.user)

require_http_methods(["POST"])
def login_employee(request):

    try:
        json_body = json.loads(request.body)        
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "body must be in json format"},
            status=HTTPStatus.BAD_REQUEST
        )
    
    try:
        username, password = json_body["username"], json_body["password"]
    except KeyError:
        return JsonResponse(
            {"error": "username and password must be provided"},
            status=HTTPStatus.BAD_REQUEST
        )
    
    user: BankUser = authenticate(request, username=username, password=password)

    if not (user.is_staff or user.is_superuser):
        return JsonResponse(
            {"erorr": "username or password is incorrect"},
             status=HTTPStatus.UNAUTHORIZED)

    login(request, user)
