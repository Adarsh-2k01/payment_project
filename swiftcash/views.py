from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from swiftcash.models import login_details,Myform,bankdetails,Card_details,feedback,dth_payment_details,h_rent,s_rent,s_main,selfbank_det,recharge_payment_his,EB_history
from swiftcash.forms import login_form,myform,bank_form,CD_CARD_FORM,feedback_form,dth_payment_form,h_rent_form,s_rent_form,s_main_form,selfbank_form,rec_payment_form,EB_form
from django.contrib.auth.decorators import login_required
# open page.
def LoginandSignup(request):
    if request.method=="POST":
        if (request.POST.get('name') and request.POST.get('login_name') and request.POST.get('email') and request.POST.get('phone_number') and
        request.POST.get('password') and  request.POST.get('location') and request.POST.get('adhaar_num') and request.POST.get('bank_acc') and request.POST.get('Gender') and request.POST.get('date')):
            saverecord              = Myform()
            saverecord.name         = request.POST.get('name')
            saverecord.login_name   = request.POST.get('login_name')
            saverecord.email        = request.POST.get('email')
            saverecord.phone_number = request.POST.get('phone_number')
            saverecord.password     = request.POST.get('password')
            saverecord.location     = request.POST.get('location')
            saverecord.adhaar_num   = request.POST.get('adhaar_num')
            saverecord.bank_acc     = request.POST.get('bank_acc')
            saverecord.Gender       = request.POST.get('Gender')
            saverecord.date         = request.POST.get('date')
            saverecord.save()
            return redirect('/select')
    else:
        return render(request,'LoginandSignup.html')
    if request.method=="POST":
        try:
            login_name=request.POST.get("login_name")
            b=Myform.objects.get(login_name=login_name)
            return render(request,'select.html',{"form":b})
        except:
            a="*YOUR NOT ONE OF US......"
            return render(request,'LoginandSignup.html',{"a":a})
    else:
        return render(request,'LoginandSignup.html')
    

#firstpage..
def select(request):
    return render(request,'select.html')

#bank page.
def bank(request):
    return render (request,'bank.html')
def selfbank(request):
    if request.method == "POST":
        if(request.POST.get('from_acc') and request.POST.get('branch') and request.POST.get('branch_code') and request.POST.get('payee_name') and  request.POST.get('payee_acc') and request.POST.get('cif') and request.POST.get('date') and request.POST.get('amount') and request.POST.get('ph_no')):
            record        = selfbank_det()
            record.acc    = request.POST.get('from_acc')
            record.branch      = request.POST.get('branch')
            record.branch_code = request.POST.get('branch_code')
            record.payee_name  = request.POST.get('payee_name')
            record.payee_acc   = request.POST.get('payee_acc')
            record.cif         = request.POST.get('cif')
            record.date        = request.POST.get('date')
            record.amount      = request.POST.get('amount')
            record.ph_no       = request.POST.get('ph_no')
            record.save()
            return redirect('/done')
    else:
        return render(request,'selfbank.html')


def form_fillup(request): 
    if request.method == "POST":
        if(request.POST.get('from_acc') and request.POST.get('to_acc') and request.POST.get('branch') and 
        request.POST.get('branch_code') and request.POST.get('payee_name') and  request.POST.get('payee_acc') and 
        request.POST.get('cif') and request.POST.get('date') and request.POST.get('amount') and request.POST.get('ph_no')):        
            saverecord             = bankdetails()
            saverecord.from_acc    = request.POST.get('from_acc')
            saverecord.to_acc      = request.POST.get('to_acc')
            saverecord.branch      = request.POST.get('branch')
            saverecord.branch_code = request.POST.get('branch_code')
            saverecord.payee_name  = request.POST.get('payee_name')
            saverecord.payee_acc   = request.POST.get('payee_acc')
            saverecord.cif         = request.POST.get('cif')
            saverecord.date        = request.POST.get('date')
            saverecord.amount      = request.POST.get('amount')
            saverecord.ph_no       = request.POST.get('ph_no')
            saverecord.save()
            return redirect('/done')
    else:
        return render(request,'form_fillup.html')

def otp(request):
    return render(request,'otp.html')
def done(request):
    return render(request,'done.html')

#credit/debit page..
def card(request):
    if request.method == "POST":
        
        if (request.POST.get('name') and request.POST.get('number') and request.POST.get('month') and request.POST.get('year') and request.POST.get('cvv')):
            saverecord=Card_details()
            saverecord.name=request.POST.get('name')
            saverecord.number=request.POST.get('number')
            saverecord.month=request.POST.get('month')
            saverecord.year=request.POST.get('year')
            saverecord.cvv=request.POST.get('cvv')
            saverecord.save()
            return redirect('/done')
    else:
        return render(request,'card.html')
def CDverify(request):
    return render(request,'CDverify.html')


#electricity bill page...
def EB(request):
    if request.method=="POST":
        if request.POST.get("state") and request.POST.get('EB'):
            saverecord=EB_history()
            saverecord.state=request.POST.get('state')
            saverecord.EB=request.POST.get('EB')
            saverecord.save()
            return redirect("/select")
    else:
        return render(request,'EB.html')

#dth bill page....
def DTH(request):
    return render(request,'DTH.html')
def dth_payment(request):
    if request.method == "POST":
        if request.POST.get('amount') and request.POST.get('Pack'):
            saverecord=dth_payment_details()
            saverecord.amount=request.POST.get('amount')
            saverecord.Pack=request.POST.get('Pack')
            saverecord.save() 
            return redirect('/done')
    else:
        return render(request,'dth_payment.html')

#recharge page.....
def Recharge(request):
    return render(request,'Recharge.html')
def recharge_payment(request):
    if request.method == "POST":
        if request.POST.get('amount') and request.POST.get('Pack'):
            saverecord=recharge_payment_his()
            saverecord.amount=request.POST.get('amount')
            saverecord.Pack=request.POST.get('Pack')
            saverecord.save() 
            return redirect('/done')
    else:
        return render(request,'recharge_payment.html')

def contact(request):
    if request.method == "POST":
        if (request.POST.get('name') and request.POST.get('email') and request.POST.get('ph_no') and request.POST.get('subject') and request.POST.get('message')):
            saverecord=feedback()
            saverecord.name=request.POST.get('name')
            saverecord.email=request.POST.get('email')
            saverecord.ph_no=request.POST.get('ph_no')
            saverecord.subject=request.POST.get('subject')
            saverecord.comment=request.POST.get('message')
            saverecord.save()
            cons=feedback.objects.all
            return render(request,'contact.html',{'cons':cons})
    else:
        return render(request,'contact.html')

   

def rent(request):
    return render(request,"rent.html")

def house_rent(request):
    if request.method == "POST":
        if (request.POST.get('Bank') and request.POST.get('bank_acc') and request.POST.get('bank_ifsc') and request.POST.get('acc_name') and request.POST.get('ph_no')):
            saverecord=h_rent()
            saverecord.Bank=request.POST.get('Bank')
            saverecord.bank_acc=request.POST.get('bank_acc')
            saverecord.bank_ifsc=request.POST.get('bank_ifsc')
            saverecord.acc_name=request.POST.get('acc_name')
            saverecord.ph_no=request.POST.get('ph_no')
            saverecord.save()
            return redirect('/done')
    return render(request,"house_rent.html")

def shop_rent(request):
    if request.method == "POST":
        if (request.POST.get('Bank') and request.POST.get('bank_acc') and request.POST.get('bank_ifsc') and request.POST.get('acc_name') and request.POST.get('ph_no')):
            saverecord=s_rent()
            saverecord.Bank=request.POST.get('Bank')
            saverecord.bank_acc=request.POST.get('bank_acc')
            saverecord.bank_ifsc=request.POST.get('bank_ifsc')
            saverecord.acc_name=request.POST.get('acc_name')
            saverecord.ph_no=request.POST.get('ph_no')
            saverecord.save()
            return redirect('/done')
    return render(request,"shop_rent.html")

def social_main(request):
    if request.method == "POST":
        if (request.POST.get('Bank') and request.POST.get('bank_acc') and request.POST.get('bank_ifsc') and request.POST.get('acc_name') and request.POST.get('ph_no')):
            saverecord=s_main()
            saverecord.Bank=request.POST.get('Bank')
            saverecord.bank_acc=request.POST.get('bank_acc')
            saverecord.bank_ifsc=request.POST.get('bank_ifsc')
            saverecord.acc_name=request.POST.get('acc_name')
            saverecord.ph_no=request.POST.get('ph_no')
            saverecord.save()
            return redirect('/done')
    return render(request,"social_main.html")
