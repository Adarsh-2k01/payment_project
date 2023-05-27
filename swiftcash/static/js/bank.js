
function check(){
		
    var bank_s=document.s_form.bank.value;
    if (bank_s==0){
        alert ("select your bank for transaction");
        return false; 
    }

    
    if (bank_s==1){
        return true;
    }
    document.querySelector(" #show-login ").addEventListener("click",function (){
    document.querySelector(" .user ").classList.add("active");
    });


    document.querySelector(".close-btn").addEventListener("click",function (){
    document.querySelector(".user").classList.remove("active");
    });

}


	function user(){
		var name=document.user_id.name.value;
		var num=document.user_id.num.value;
		var pin=document.user_id.pin.value;

		if(name==null||name==""){
			alert("type your username....");
			return false;
		}

		if(num==null||num==""){
			alert("type your phone number....");
			return false;
		}

		if(pin==null||pin==""){
			alert("type your pin code....");
			return false;
		}
	}