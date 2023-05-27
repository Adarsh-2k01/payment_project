let btnclr=document.querySelector("button");
let inputs=document.querySelector("input");
btnclear.addEventListener("click", () =>{
inputs.foreach(input => input.value ="");
});

        function CDform(){
            var name      =document.cd_form.username.value;
            var d_valid   =document.cd_form.valid_date.value;
            var d_expiry  =document.cd_form.expiry_date.value;
            var pinnumber =document.cd_form.pin.value;
            var cvv       =document.cd_form.cvv.value;
            var check     =document.cd_form.agree.value;
            

            if (name==null||name==""){
                alert("name can't be blank");
                return false;}

            if(d_valid.length!=6)
                {
                    alert("please enter correct month&year");
                    return false;
                } 

            if(d_expiry.length!=6)
                {
                    alert("please enter correct month&year");
                    return false;
                }    
            
            if(pinnumber.length!=16)
                {
                    alert("enter correct pin ");
                    return false;
                }
            if(cvv.length!=3)
                {
                    alert("enter correct cvv");
                    return false;
                }
        
            }