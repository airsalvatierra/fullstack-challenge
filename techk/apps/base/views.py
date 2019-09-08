from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('Hello, world!')
    return render(request,'index.html')

# def home_page(request):
#     roles = KerSocioRol.objects.filter(socio=request.user).order_by('rol')
#     if request.user.last_login is None:
#         return HttpResponseRedirect(reverse('change_password2'))
#     context = {
#         'roles':roles,
#     }
#     return render(request,'index.html',context)
