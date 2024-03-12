from django.shortcuts import render
from .models import TbLogin

# Create your views here.
def user_login(request):
    if request.method == "POST":
        unm = request.POST.get("username")
        pwd = request.POST.get("password")
        obj = TbLogin.objects.filter(username=unm, password=pwd)
        for x in obj:
            ty = x.type
            if ty == "patient":
                request.session['tid'] = ty
                return render(request, 'patient.html',{'username': x.username, 'type': ty})
            elif ty == "doctor":
                request.session['tid']=ty
                return render(request, 'doctor.html',{'username': x.username, 'type': ty})
            elif ty == "pharmacist":
                request.session['tid'] = ty
                return render(request, 'pharmacist.html',{'username': x.username, 'type': ty})
    return render(request,'userlogin.html')


