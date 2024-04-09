from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
  
  features = Feature.objects.all()
  return render(request, 'index.html', {'features':features}) 
  """
  feature1 = Feature()
  feature1.name ='Fast'
  feature1.id= 0
  feature1.details = 'The latest official version is 5.0.3. Read the 5.0.3 release notes, then install it with pip:'
  feature1.is_true = True

  feature2 = Feature()
  feature2.name ='XXX'
  feature2.id= 1
  feature2.details = 'pretty fuck'
  feature2.is_true = True

  feature3 = Feature()
  feature3.name ='Slow'
  feature3.id= 2
  feature3.details = 'This is only for experienced users who want to try incoming changes and help identify bugs before an official release. Get it using this shell command, which requires'
  feature3.is_true = False

  feature4 = Feature()
  feature4.name ='Dheere'
  feature4.id= 3
  feature4.details = 'Feature releases (A.B, A.B+1, etc.) will happen roughly every eight months. These releases will contain new features, improvements to existing features, and such. '
  feature4.is_true = True

  feature5 = Feature()
  feature5.name ='Reliable'
  feature5.id= 4
  feature5.details = 'fhdhdhdhdhdghfgfghghdthdtyey'
  features = [feature1, feature2,feature3,feature4]
  """
  """  context ={
        'name' : 'Khan',
        'age'  : 34,
        'nationality' : 'British'

  }
    
    return render(request,'index.html',context)
"""
  #return render(request, 'index.html',{'features': features })  #return render(request, 'index.html',{'feature1': feature1, 'feature2': feature2, 'feature3': feature3,'feature4':feature4})

   #return render(request, 'index.html',{'name':name})
    #return HttpResponse('<h1>Hey , Welcome </h1>')

def counter(request):
    posts = [1,2,3,4,5,'tim','tom','john']
   
   #words = request.POST['words']
    #amount_of_words = len(words.split()) 
    
    #return render(request,'counter.html',{'amount_of_words':amount_of_words})
    return render(request,'counter.html',{'posts':posts})
def login(request):
   
   if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username = username ,password=password)
    if user is not None:
     auth.login(request,user)
     return redirect('/')
    else:
     messages.info(request,'Credentials Invalid')
     return redirect('login')
    
     
      
      
   else:
     return render(request, 'login.html')
   


def logout(request):
  auth.logout(request)
  return redirect('/')
  
   

   


def register(request):
 if request.method == 'POST':
   username = request.POST['username']
   email = request.POST['email']
   password = request.POST['password']
   password2 = request.POST['password2']

   if password == password2:
     if User.objects.filter(email=email).exists():
       messages.info(request,'Email Already Used')
       return redirect('register')
     elif User.objects.filter(username=username ).exists():
       messages.info(request,'Username already exists')
       return redirect('register')
     else:
       user = User.objects.create_user(username=username,email=email,password=password)
       user.save();
       return redirect('login')
     
   else:
        messages.info(request,'Pass Not Matched')
        return redirect('register')
 


     
     
   
 else:
    return render(request,'register.html')
 
 
def post(request,pk):
  return render(request,'post.html',{'pk': pk})