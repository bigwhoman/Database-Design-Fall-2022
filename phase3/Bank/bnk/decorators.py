from functools import wraps
from django.http import JsonResponse
def employee_required(func):    
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return func(request, *args, **kwargs)
        return JsonResponse(
            {"error": "not allowed"},
            status=403)
    return wrapper