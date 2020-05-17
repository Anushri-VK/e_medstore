from django.shortcuts import render,redirect
from django.contrib import messages
from medicines.models import Registration,Contact,MedicineOrdered,Askdoctor,Contactlogin
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import date
from datetime import datetime
from datetime import timedelta


def index(request):
	parameters = {'name': 'medicine', 'place': 'it'}
	return render(request,"index.html")

def signup(request):
	if request.method=="POST":
		user=request.user
		fname=request.POST["fname"]
		mname=request.POST["mname"]
		lname=request.POST["lname"]
		email=request.POST["email"]
		gender=request.POST["gender"]
		selphone=request.POST["selphone"]
		contactnumber=request.POST["contactnumber"]
		password=request.POST["password"]
		cpassword=request.POST["cpassword"]
		address=request.POST["address"]
		user=User.objects.create_user(username=fname,password=password,email=email)
		login(request,user)
		subject='Your account has been created successfully!'
		message=f'Registration MedsOn,Thank you {user.username} for registration. Happy Shopping'
		email_from=settings.EMAIL_HOST_USER
		recipient_list=[user.email,]
		send_mail( subject,message,email_from,recipient_list)
		if password==cpassword:
			signup=Registration.objects.create(fname=fname,mname=mname,lname=lname, email=email, gender=gender,
				selphone=selphone,contactnumber=contactnumber,password=password,
				cpassword=cpassword,address=address
				)
		else:
			messages.success(request, 'Password doesnt match')
			return redirect('/signup/')
		return redirect("/contactuslogin/")
	return render(request,'signup.html')
	

def signin(request):
	print("hi")
	if request.method=="POST":
		print("hello")
		username=request.POST["username"]
		print(username)
		password=request.POST["password"]
		print(password)

		user=authenticate(username=username,password=password)

		if user!=None:
			login(request,user)
			return redirect("/store/")

	return render(request,"signin.html")


def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
	if request.method == "POST":
		name= request.POST["name"]
		email= request.POST["email"]
		message = request.POST["message"]
		contactus = Contact.objects.create(name=name ,email=email, message=message)
		contactus.save()
		messages.success(request, 'Your message has been send!!')
	return render(request , 'contactus.html')
	

def store(request):
	a=[]
	if request.method == "POST":
		user= request.user
		Combiflam=  request.POST.get("Combiflam",0)
		a.append(int(Combiflam))
		Paracetamol=  request.POST.get("Paracetamol",0)
		a.append(int(Paracetamol))
		Cofsils=  request.POST.get("Cofsils",0)
		a.append(int(Cofsils))
		DigeneTablet=  request.POST.get("DigeneTablet",0)
		a.append(int(DigeneTablet))
		DigeneGel=  request.POST.get("DigeneGel",0)
		a.append(int(DigeneGel))
		Hajmola=  request.POST.get("Hajmola",0)
		a.append(int(Hajmola))
		Seacod=  request.POST.get("Seacod",0)
		a.append(int(Seacod))
		Shelcal=  request.POST.get("Shelcal",0)
		a.append(int(Shelcal))
		Crocin=  request.POST.get("Crocin",0)
		a.append(int(Crocin))
		Lubrifresh= request.POST.get("Lubrifresh",0)
		a.append(int(Lubrifresh))
		Dettol= request.POST.get("Dettol",0)
		a.append(int(Dettol))
		Ashwagandha= request.POST.get("Ashwagandha",0)
		a.append(int(Ashwagandha))
		Moov= request.POST.get("Moov",0)
		a.append(int(Moov))
		Zandu= request.POST.get("Zandu",0)
		a.append(int(Zandu))
		Vicks= request.POST.get("Vicks",0)
		a.append(int(Vicks))
		Chyawanprash= request.POST.get("Chyawanprash",0)
		a.append(int(Chyawanprash))
		totalSum= request.POST.get("totalSum")
		all_medicines=MedicineOrdered.objects.filter(user=user)
		Combiflam = int(Combiflam) * 28
		Paracetamol = int(Paracetamol) * 30
		Cofsils = int(Cofsils) * 30
		DigeneTablet = int(DigeneTablet) * 17
		DigeneGel = int(DigeneGel) * 100
		Hajmola = int(Hajmola) * 32
		Seacod = int(Seacod) * 272
		Shelcal =int(Shelcal) * 86
		Crocin =int(Crocin) * 15
		Lubrifresh =int(Lubrifresh) * 99
		Dettol =int(Dettol) * 266
		Ashwagandha =int(Ashwagandha) * 296
		Moov =int(Moov) * 160
		Zandu =int(Zandu) * 40
		Vicks =int(Vicks) * 124
		Chyawanprash =int(Chyawanprash) * 309
		totalSum = Combiflam+Paracetamol+Cofsils+DigeneTablet+DigeneGel+Hajmola+Seacod+Shelcal+Crocin+Lubrifresh+Dettol+Ashwagandha+Moov+Zandu+Vicks+Chyawanprash
		store = MedicineOrdered.objects.create(
			Combiflam=Combiflam,Paracetamol=Paracetamol,Cofsils=Cofsils,
			DigeneTablet=DigeneTablet,DigeneGel=DigeneGel,Hajmola=Hajmola,
			Seacod=Seacod, Shelcal=Shelcal, Crocin=Crocin, Lubrifresh=Lubrifresh,
			Dettol=Dettol, Ashwagandha=Ashwagandha, Moov=Moov, Zandu=Zandu,Vicks=Vicks,
			Chyawanprash=Chyawanprash,totalSum=totalSum)
	
		store.save()
		return render(request,'cart.html',{'a':a,'totalSum':totalSum})
	return render(request,'store.html')
	

def askadoctor(request):
	if request.method == "POST":
		question = request.POST["question"]
		looking = request.POST["looking"]
		email = request.POST["email"]
		selphone = request.POST["selphone"]
		contactnumber = request.POST["contactnumber"]
		askadoctor = Askdoctor.objects.create(question=question, looking=looking, email=email,
			selphone=selphone, contactnumber=contactnumber)
		askadoctor.save()
		messages.success(request, 'Your query is successfully registered! You will recieve a confirmation email regarding your appointment. Thanks')
		subject='Appointment Confirmation MedsOn'
		message= f'Your details has been recieved.\n\nCategory:\n{askadoctor.looking}\n\nYour query:\n {askadoctor.question}  \n\nYour registered mobile number:\n {askadoctor.selphone} {askadoctor.contactnumber} \n\nWe will contact you once your request is reviewed by our doctors.\n\nThanks\nMedsOn'
		email_from=settings.EMAIL_HOST_USER
		recipient_list=[askadoctor.email,]
		send_mail( subject,message,email_from,recipient_list)
	return render(request, 'askadoctor.html')


def contactuslogin(request):
	if request.method == "POST":
		name=request.POST["name"]
		email=request.POST["email"]
		message=request.POST["message"]
		contactuslogin=Contactlogin.objects.create(name=name ,email=email, message=message)
		contactuslogin.save()
		messages.success(request, 'Your message has been send!!')
	return render(request , 'contactuslogin.html')

def aboutuslogin(request):
    return render(request, 'aboutuslogin.html')


def cart(request):
	obj=MedicineOrdered.objects.filter(user=request.user)
	return render(request, 'cart.html', {'obj':obj})



	
def orderplace(request):
	obj1=MedicineOrdered.objects.filter()
	obj2=Registration.objects.filter()
	delidate=date.today() + timedelta(days=3)
	return render(request, 'orderplace.html')
	subject='Your MedsOn Order is Confirmed'
	message=f'Hi {obj2.fname}\n\nYour MedsOn order confirmation\n\nHere are your order details:\n__________________________\n\nOrder Date:{date.today()}\n\nOrder Summary:\n\n\nShipping To:\n_____________\n{obj2.address}\n\n\nYou can expect to receive items in your order by:{delidate}'
	email_from=settings.EMAIL_HOST_USER
	recipient_list=[orderplace.email,]
	send_mail( subject,message,email_from,recipient_list)
