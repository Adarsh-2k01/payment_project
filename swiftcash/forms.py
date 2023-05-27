from django import forms
from django.forms import ModelForm
from swiftcash.models import login_details,Myform,bankdetails,Card_details,feedback,dth_payment_details,h_rent,s_rent,s_main,selfbank_det,recharge_payment_his,EB_history

class login_form(ModelForm):
    class Meta:
        model=login_details
        fields=['login_name','password']


class myform(ModelForm):
    class Meta:
        model=Myform
        fields=['name','login_name','email','phone_number','password','location','adhaar_num','bank_acc','Gender','date']


class bank_form(ModelForm):
    class Meta:
        model=bankdetails
        fields=['from_acc','to_acc','branch','branch_code','payee_name','payee_acc','cif','date','amount','ph_no']

class selfbank_form(ModelForm):
    class Meta:
        model=selfbank_det
        fields=['acc','branch','branch_code','payee_name','payee_acc','cif','date','amount','ph_no']

class CD_CARD_FORM(ModelForm):
    class Meta:
        model=Card_details
        fields=['name','number','month','year','cvv']

class feedback_form(ModelForm):
    class Meta:
        model=feedback
        fields=['name','email','ph_no','subject','comment']

class dth_payment_form(ModelForm):
    class Meta:
        model=dth_payment_details
        fields=['Pack','amount']


class rec_payment_form(ModelForm):
    class Meta:
        model=recharge_payment_his
        fields=['Pack','amount']

class h_rent_form(ModelForm):
    class Meta:
        model=h_rent
        fields=['Bank','bank_acc','bank_ifsc','acc_name','ph_no']

class s_rent_form(ModelForm):
    class Meta:
        model=s_rent
        fields=['Bank','bank_acc','bank_ifsc','acc_name','ph_no']

class s_main_form(ModelForm):
    class Meta:
        model=s_main
        fields=['Bank','bank_acc','bank_ifsc','acc_name','ph_no']

class EB_form(ModelForm):
    class meta:
        model=EB_history
        fields=["state","EB"]       
