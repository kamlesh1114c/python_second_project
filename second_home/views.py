from django.shortcuts import render
from .models import Contact,User,Hotel_Ditaile
# Create your views here.def

def index(request):
	if request.method=="POST":
		Contact.objects.create(
			name=request.POST['name'],
			email=request.POST['email'],
			subject=request.POST['subject'],
			message=request.POST['message'],
		)
		msg="Contact saved Successfully"
		return render (request,'index.html',{'msg':msg})
	else:
		return render (request,'index.html')	

def signup(request):
	if request.method == "POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg="Email Already registered"
			return render(request,'signup.html',{'msg':msg})
		except Exception as e:
			print(e)
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					username=request.POST['username'],
					email=request.POST['email'],
					password=request.POST['password'],
				)
				msg="SignUp Successfully"
				return render(request,'index.html',{'msg':msg})
			else:
				msg="Password And Confirm Password Doest Not match"
				return render(request,'signup.html',{'msg':msg})			
	else:	
		return render(request,'signup.html')

def login(request):
	if request.method == "POST":
		try:
			user=User.objects.get(email=request.POST['email'],
				password=request.POST['password'])
			request.session['email']=user.email
			request.session['profile_pic']=user.profile_pic.url
			return render(request,'index.html')
		except:
			msg="Email or Password Is Incorrect"
			return render (request,'login.html',{'msg':msg})
	else:
		return render (request,'login.html')	

def logout(request):
	try:
		del request.session['email']
		del request.session['profile_pic']
		return render (request,'index.html')
	except:
		return render (request,'index.html')

def edit_profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.name=request.POST['name']
		user.email=request.POST['email']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		user.request.session['profile_pic']=user.profile_pic.url
		return render(request,'edit_profile.html',{'user':user})
	else:			
		return render(request,'edit_profile.html',{'user':user})

def forgot(request):
	if request.method == "POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			subject = 'OTP For Forgot Password'
			otp=random.randint(1000,9999)
			message = 'Hello'+user.name+',Your OPT For  Forgot Password Is'+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'verify_otp.html',{'otp':otp,'email':user.email})
		except: 	
			msg="Enter Email Not Registered"
			return render(request,'forgot.html',{'msg':msg})
	else:	
		return render(request,'forgot.html')

def verify_otp(request):
	return render(request,'index.html')	