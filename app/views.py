from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse
from django.db.models.functions import Length
def insert_dept(request):
    deno=input('enter deptno: ')
    dn=input('enter deptname: ')
    loc=input('enter location: ')
    DO=Dept.objects.get_or_create(deptno=deno,name=dn,loc=loc)[0]
    DO.save()
    return HttpResponse('dept data updated sucessfully') 


def insert_emp(request):
    empno=input('enter empno: ')
    ename=input('enter ename: ')
    job=input('enter job: ')
    mgr=input('enter mgr: ')
    hiredate=input('enter hiredate: ')
    sal=input('enter sal: ')
    comm=input('enter comm: ')
    deno=input('enter deno: ')
    dn=input('enter deptname: ')
    loc=input('enter location: ')
    DO=Dept.objects.get_or_create(deptno=deno,name=dn,loc=loc)[0]
    DO.save()
    EO=Emp.objects.get_or_create(empno=empno,ename=ename,job=job,mgr=mgr,hiredate=hiredate,sal=sal,comm=comm,deptno=DO)[0]
    EO.save()

    return HttpResponse('emp data inserted sucessfully')


def display_dept(request):
    LOD=Dept.objects.all()
    d={'department':LOD}
    return render(request,'display_dept.html',context=d)

def display_emp(request):
    LOE=Emp.objects.all()
    LOE=Emp.objects.order_by(Length('ename').desc())
    LOE=Emp.objects.order_by(Length('ename'))
    d={'employee':LOE}
    return render(request,'display_emp.html',context=d)