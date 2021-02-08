from django.shortcuts import render, redirect
from instawin.models import *
from django.db.models import Sum
from django.contrib.auth import authenticate, logout, login

# Create your views here.x

def index(request):
    return render(request, 'index.html')

def dashboard(request):

    # Fetch Data:
    res = tblresult1.objects.filter(resultt1=0)
    gid = tblresult1.objects.order_by('-id')[:1]
    tim = tblLiveTime.objects.order_by('-id')[:1]
    us_co = tblAGameone.objects.count()
    total_paid1 = list(tblAGameone.objects.aggregate(Sum('Bid1')).values())[0]
    total_paid2 = list( tblAGameone.objects.aggregate( Sum( 'Bid2' ) ).values() )[0]
    r = {'res':res, 'gid':gid, 'tim':tim, 'us_co':us_co, 'total_paid1':total_paid1, 'total_paid2':total_paid2}

    # update result
    error = ""
    if request.method =='POST':
        r = request.POST['resultt1']
        try:
            tblresult1.objects.update(resultt1=r)
            error = "no"
        except:
            error= "yes"
        r = {'error':error}


    return render(request, 'dashboard.html', r)
# Logout Page Method:

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')