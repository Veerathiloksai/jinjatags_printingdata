from django.shortcuts import render

# Create your views here.

def sachin(request):
    d={'name':'sachin','age':51,'year':1989,'centuries':100}
    return render(request,'cricketer.html',context=d)
