from django.shortcuts import render
from student.models import Student
# Create your views here.
def index(request):
    return render(request, 'index.html')
def get(request):
    return render(request, 'get.html')
def addget(request):
    if request.method == 'POST': #request.POST.get()
        n1=int(request.GET.get('num1'))
        n2=int(request.GET.get('num2'))
        sum=n1+n2   
        return render(request, 'result.html', {'result': sum})
def post(request):
    return render(request,'post.html')
def addpost(request): #request.POST.get()
    n1=int(request.POST.get('num1'))
    n2=int(request.POST.get('num2'))
    sum=n1+n2  
    return render(request,'post.html',{'result':sum})
def registration(request):
    return render(request, 'registration.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def insert(request):
    vname=request.POST.get('name')
    vemail=request.POST.get('email')
    vphone=request.POST.get('phone')
    vpassword=request.POST.get('password')
    vaddress=request.POST.get('address')
    s=Student(name=vname,email=vemail,phone=vphone,password=vpassword,address=vaddress)
    s.save() #method to insert data into database
    return render(request,'registration.html',{})