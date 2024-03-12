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
                return render(request, 'patient.html',{'username': x.username, 'type': ty})
            elif ty == "doctor":
                return render(request, 'doctor.html',{'username': x.username, 'type': ty})
            elif ty == "pharmacist":
                return render(request, 'pharmacist.html',{'username': x.username, 'type': ty})
    return render(request,'userlogin.html')


