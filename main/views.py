from django.shortcuts import render ,redirect
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        FullName = request.POST['FullName']
        FirstName = request.POST['FirstName']
        Username = request.POST['Username']
        EmailId = request.POST['EmailId']
        password = request.POST['password']
        
        User.objeact.create_user(FullName=FullName,FirstName=FirstName, Username=Username,password=password,EmailId=EmailId)
        return redirect('/')
    return render(request,"register.html")
