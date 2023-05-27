function check(){
    var F_acc=document.bd.from_acc.value;
    var T_acc=document.bd.to_acc.value;
    var name=document.bd.payee_name.value;
    var acc_no=document.bd.payee_acc.value;
    var rs=document.bd.amount.value;
    var nall=document.bd.date.value;

    if(F_acc.length!=15){
        alert("enter from account number");
        return false;
    }

    if(T_acc.length!=15){
        alert("enter to account number");
        return false;
    }

    if(name==null||name==""){
        alert("enter payee name");
        return false;
    }

    if(acc_no.length!=15){
        alert("enter payee account number");
        return false;
    }

    if(rs==null||rs==""){
        alert("enter the amount to send");
        return false;
    }

    if(nall==null||nall==""){
        alert("enter date of transaction");
        return false;
    }

}