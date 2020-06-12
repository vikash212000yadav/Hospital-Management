from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Appointment
from accounts.models import Doctor,Patient
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def appointments(request):
    if request.user.last_name=="Patient":
        pro=Patient.objects.filter(user=request.user).first()
        ap=Appointment.objects.filter(patient=pro).all()
        c={'pro':pro,'ap':ap}
    if request.user.last_name=="Doctor":
        pro=Doctor.objects.filter(user=request.user).first()
        ap=Appointment.objects.filter(doctor=pro).all()
        c={'pro':pro,'ap':ap}
             
    return render(request,"appointments/appointments.html",c)

@login_required
def reception(request):
    ap=Appointment.objects.all()
    p=Patient.objects.all()
    tot=len(ap)
    pending=len(Appointment.objects.filter(status="Pending").all())
    com=len(Appointment.objects.filter(status="Completed").all())
    c={'ap': ap ,'p':p,'tot':tot,'pend':pending,'com':com}             
    return render(request,"appointments/reception.html",c)
@login_required
def deletepat(request):
    if request.method=='POST':
        pid=request.POST['pid']
        px=Patient.objects.filter(pid=pid).first()
        us=User.objects.filter(username=px.user.username).first()
        us.delete()
        return redirect("appointments")
    ap=Appointment.objects.all()
    p=Patient.objects.all()
    c={'ap': ap ,'p':p}             
    return render(request,"appointments/reception.html",c)

@login_required
def createpat(request):
    if request.method=='POST':        
        try:
            _, file = request.FILES.popitem()
            file = file[0]
            image = file
        except:
            pass
        finally:
            fname=request.POST['name']
            email=request.POST['email']
            phone=request.POST['phone']
            gender=request.POST['gender']
            age=request.POST['age']
            add=request.POST['address']
            bg=request.POST['bloodgroup']
            casepaper=request.POST['casepaper']
            if User.objects.filter(username=email).exists():
                messages.info(request,"Email Id already Exists!")
                return redirect('crtpat')
            else:
                user=User.objects.create_user(first_name=fname,last_name='Patient',username=email,email=email)
                pro=Patient(user=user,phone=phone,gender=gender,age=age,address=add,bloodgroup=bg,casepaper=casepaper,image=image)
                pro.save()
                return redirect('reception')
    return render(request,'appointments/crtpat.html')

@login_required
def updatepat(request):
    if request.method=='POST':
        pid=request.POST['pid']
        pro=Patient.objects.filter(pid=pid).first()
        return render(request,'accounts/uprofile.html',{'pro':pro})

@login_required
def setapt(request):
    d=Doctor.objects.all()
    p=Patient.objects.all()
    da=[]
    y=[]
    h=[]
    m=['00','15','30','45']
    for x in range(2020,2031):
        y.append(x)
    for x in range(1,32):
        da.append(x)
    for x in range(1,13):
        h.append(x)
    if request.method=='POST':
        hours=request.POST['hours']
        min=request.POST['min']
        am=request.POST['am']
        time=hours+" : "+min+" "+am
        doc=request.POST['doc']
        pat=request.POST['pat']
        sta=request.POST['status']
        dat=request.POST['d']
        month=request.POST['m']
        year=request.POST['y']
        date=dat+"-"+month+"-"+year
        user1=User.objects.filter(first_name=pat).first()
        user2=User.objects.filter(first_name=doc).first()
        pa=Patient.objects.filter(user=user1).first()
        do=Doctor.objects.filter(user=user2).first()
        a=Appointment.objects.create(patient=pa,doctor=do,time=time,date=date,status=sta)
        a.save()
        return redirect('reception')
    return render(request,'appointments/setapt.html',{'d':d,'p':p,'m':m,'da':da,'y':y,'h':h})
