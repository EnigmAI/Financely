from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect("basic_app:index")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator
# 
# def search_bar(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         if request.is_ajax():
#             res = None
#             data = request.POST.get('searchData')
#             item = getStockInfo(data)
#             if len(item)>0 and len(data):
#                 res = item
#             else:
#                 res = 'No stocks found..'
#
#             #print(data)
#             return JsonResponse({'data':res})
#         else:
#             return view_func(request, *args, **kwargs)
#
#     return wrapper_func


# def admin_only(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name
#
#         if group == 'Client':
#             return redirect('user-page')
#
#         if group == 'Admin':
#             return view_func(request, *args, **kwargs)
#
#     return wrapper_function
