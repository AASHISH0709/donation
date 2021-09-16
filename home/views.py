from django.shortcuts import render,HttpResponse

# Create your views here.
import razorpay
from datetime import datetime
from .models import User_contact
from .models import  Donation
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages

def index(request):
    return render(request,"index.html")

def donate(request):
    if request.method=="POST":
        name=request.POST.get("name")
        amount=int(request.POST.get("amount"))*100
        if(len(name)!=0 and amount<= 0 ):            
            return render(request,"donate.html")
            messages.success(request, 'Please enter valid details')
            
        email=request.POST.get("email")
        request.session['amt']=amount
        client=razorpay.Client(auth=("rzp_test_SGOEshaOuD7kNT","2Vc5G9ziCXPIzgZr1RMglLkq"))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        print(payment)
        donation=Donation(name=name,amount=amount,email=email,payment_id=payment['id'])
        donation.save()
        return render(request,"donate.html",{'payment':payment})

    return render(request,"donate.html")

def contact_us(request):
    if request.method=="POST":
        name1=request.POST.get("name1")
        email1=request.POST.get("email1")
        phone1=request.POST.get("phone1")
        msg1=request.POST.get("msg1")
        contact=User_contact(name1=name1,email1=email1,phone1=phone1,msg1=msg1,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent!')

    return render(request,"contactus.html")

@csrf_exempt
def success(request):
    context={}
    ok1=request.session['amt']
    context['ok1']=int(ok1/100)
    if request.method=="POST":
        a=request.POST
        order_id=""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id=val
                break
        print(order_id)
        user=Donation.objects.filter(payment_id=order_id).first()
        user.paid=True
        user.save()
        msg_plain=render_to_string('email.txt')
        msg_html=render_to_string('email.html')
        send_mail("Your donation has been recived", msg_plain,settings.EMAIL_HOST_USER,
        [user.email],html_message=msg_html)

    return render(request,"success.html",context)

