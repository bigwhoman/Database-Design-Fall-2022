import json
from http import HTTPStatus
from datetime import timedelta
from bnk.models import BankUser, Contract, Salon, TimePlan, SafeBox
from bnk.decorators import employee_required

from django.forms.models import model_to_dict
from django.db.models import DurationField
from django.views import View
from django.utils import timezone
from django.db.models import Sum, F, Exists, OuterRef
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import time

require_http_methods(["GET"])
@login_required
def get_safeboxes(request):
    user = request.user
    salons = Salon.objects.select_related().all()
    res = dict()
    user_credit = user.accounts.aggregate(credit=Sum("credit"))["credit"] or 0
    for salon in salons:
        res[salon.id] = dict()
        safeboxes = salon.safeboxes.annotate(is_available=~Exists(Contract.objects.filter(is_valid=True, safebox=OuterRef("safebox_number"), salon=OuterRef("salon_id"))))
        for safebox in safeboxes:
            res[salon.id][safebox.safebox_number] = safebox.is_available and salon.security_level.maximum_amount <= user_credit
    return JsonResponse(res)

require_http_methods(["GET"])
@login_required
@employee_required
def get_contracts(request):
    c = Contract.objects.all()
    out_contract = []
    for obj in c:
        
        t = model_to_dict(obj)
        t["isvalid"] = obj.is_valid and obj.start_date >= timezone.now() - timedelta(days=30 * obj.timeplan.time)
        if not obj.is_valid or not t["isvalid"] :
            continue
        # dt = datetime.now()
        timestamp = time.mktime(timezone.now().timetuple())
        timestamp2 = time.mktime(obj.start_date.timetuple())
        timestamp5 = time.mktime((obj.start_date+timedelta(days=30 * obj.timeplan.time)).timetuple())
        t["remaining_time"] = timedelta(seconds = max((timestamp5 - timestamp),0)).__str__().split(".")[0]
        out_contract.append(t)
    return JsonResponse({"contracts":out_contract})

require_http_methods(["DELETE"])
@login_required
@employee_required
def cancel_contract(request):
    try:
        json_body = json.loads(request.body)        
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "body must be in json format"},
            status=HTTPStatus.BAD_REQUEST
        )
    try:
        salon_id, safebox_id = json_body["salon"], json_body["safebox"]
    except KeyError:
        return JsonResponse(
            {"error": "username and password must be provided"},
            status=HTTPStatus.BAD_REQUEST
        )
    employee: BankUser = request.user
    salon: Salon = employee.salons.select_related().filter(id=salon_id).first()
    if salon is None:
        return JsonResponse(
            {"error": "no salon with this id"},
            status=HTTPStatus.FORBIDDEN
        )
    safebox: SafeBox = salon.safeboxes.filter(safebox_number=safebox_id).first()
    if safebox is None:
        return JsonResponse(
            {"error": "no safebox with this id in salon"},
            status=HTTPStatus.BAD_REQUEST
        )
    contract: Contract = Contract.objects.filter(salon_id=salon, safebox_id=safebox_id, is_valid=True).first()
    if contract is None:
        return JsonResponse(
            {"message": "the safebox is not occupied"},
            status=HTTPStatus.OK
        )
    contract.is_valid = False
    contract.save()
    return JsonResponse(
            {"message": "success"},
            status=HTTPStatus.OK
        )
require_http_methods(["POST"])
@login_required
@employee_required
def give_safebox_to_customer(request):
    try:
        json_body = json.loads(request.body)        
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "body must be in json format"},
            status=HTTPStatus.BAD_REQUEST
        )
    try:
        username, salon_id, safebox_id, timeplan = json_body["username"], json_body["salon"], json_body["safebox"], json_body["timeplan"]
    except KeyError:
        return JsonResponse(
            {"error": "username and password must be provided"},
            status=HTTPStatus.BAD_REQUEST
        )
    user = BankUser.objects.filter(username=username).first()
    if user is None:
        return JsonResponse(
            {"error": "user does not exist"},
            status=HTTPStatus.BAD_REQUEST
        )
    employee: BankUser = request.user
    salon: Salon = employee.salons.select_related().filter(id=salon_id).first()
    if salon is None:
        return JsonResponse(
            {"error": "no named salon !"},
            status=HTTPStatus.NOT_FOUND
        )
    safebox: SafeBox = salon.safeboxes.filter(safebox_number=safebox_id).first()
    if safebox is None:
        return JsonResponse(
            {"error": "no named safebox"},
            status=HTTPStatus.NOT_FOUND
        )
    contract = Contract.objects.filter(salon_id=salon, safebox_id=safebox_id, is_valid=True).first()
    if contract is not None:
        return JsonResponse(
            {"error": "already reserved"},
            status=HTTPStatus.NOT_FOUND
        )
    user_credit = user.accounts.aggregate(credit=Sum("credit"))["credit"]
    if salon.security_level.maximum_amount > user_credit:
        return JsonResponse(
            {"error": "user can not rent safebox in this salon due to low credit"},
            status=HTTPStatus.BAD_REQUEST
        )
    
    timeplan = TimePlan.objects.filter(time=timeplan).first()
    daily_cost = safebox.price_group.daily_cost
    contract = Contract.objects.create(salon_id=salon_id, safebox_id=safebox_id,
                            timeplan=timeplan, customer=user,
                            paid_amount=daily_cost*30*timeplan.time*round(1 - timeplan.discount/100))
    return JsonResponse(
        {"message" : model_to_dict(contract)}, status=HTTPStatus.CREATED
    )
    

@method_decorator(login_required, name="dispatch")
@method_decorator(employee_required, name="dispatch")
class EditCustomerView(View):
    # register a new customer
    def post(self, request):
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
        if BankUser.objects.filter(username=username).first() is None:
            user = BankUser(username=username)
            user.set_password(password)
            user.save()
            return JsonResponse(
            {"message" : model_to_dict(user, exclude=["password"])},
            status=HTTPStatus.OK
            ) 
        else:
            return JsonResponse(
                {"error": "username already exists"},
                status=HTTPStatus.BAD_REQUEST
            )
    # edit customer profile
    def patch(self, request):
        try:
            json_body = json.loads(request.body)        
        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "body must be in json format"},
                status=HTTPStatus.BAD_REQUEST
            )
        try:
            username = json_body["username"]
        except KeyError:
            return JsonResponse(
                {"error": "username must be provided"},
                status=HTTPStatus.BAD_REQUEST
            )
        user = BankUser.objects.filter(username=username).first()
        if user is None or user.is_staff or user.is_superuser:
            return JsonResponse({"error": "you can not patch non customer user"},  status=HTTPStatus.FORBIDDEN)
        user.first_name = json_body.get("first_name", user.first_name)
        user.last_name = json_body.get("last_name", user.last_name)
        if "new_password" in json_body:
            user.set_password(json_body["new_password"])
        if "new_username" in json_body : 
            new_username = json_body["new_username"]
            if BankUser.objects.filter(username=new_username).first() is None:
                user.username = new_username
            else:
                return JsonResponse(
                    {"error": "username already exists"},
                    status=HTTPStatus.BAD_REQUEST
                )
        user.save()
        return JsonResponse(
            {"message" : model_to_dict(user, exclude=["password"])},
            status=HTTPStatus.OK
        )
        
    # delete customer
    def delete(self, request):
        try:
            json_body = json.loads(request.body)        
        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "body must be in json format"},
                status=HTTPStatus.BAD_REQUEST
            )
        try:
            username = json_body["username"]
        except KeyError:
            return JsonResponse(
                {"error": "username must be provided"},
                status=HTTPStatus.BAD_REQUEST
            )
        user = BankUser.objects.filter(username=username).first()
        if user is None or user.is_staff or user.is_superuser:
            return JsonResponse({"error": "you can not delete non customer user"},status=HTTPStatus.FORBIDDEN)
        else:
            user.delete()
            return JsonResponse({"message": "customer deleted"},status=HTTPStatus.OK)
        


require_http_methods(["POST"])
@login_required
def register_employee(request):
    # only admin can register employee
    if not request.user.is_superuser:
        return JsonResponse(
            {"error":"not allowed"}, status=HTTPStatus.FORBIDDEN
        )
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
    try :
        user.save()
    except Exception as e:
        return JsonResponse(
            {"error": "user already exists"},
            status=HTTPStatus.BAD_REQUEST
        )
    return JsonResponse(
        {"message" : model_to_dict(user, exclude=["password", "email"])}, status=HTTPStatus.CREATED
    )


require_http_methods(["POST"])
@login_required
def logout_bankuser(request):
    logout(request)
    return JsonResponse(
            {"message": "logged out"},
            status=200
        )
    

require_http_methods(["POST"])
def login_bankuser(request):

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
    if user is not None: 
        login(request, user)
        return JsonResponse(
            {"message":"success"},
            status=200
        )
    else :
        return JsonResponse(
            {"error": "wrong username or password"},
            status=HTTPStatus.BAD_REQUEST
        )
