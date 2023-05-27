/*popup1 js*/
document.querySelector(" #money_transfer ").addEventListener("click",function (){
    document.querySelector(" .pop ").classList.add("active");
    });
    document.querySelector(".close-btn").addEventListener("click",function (){
    document.querySelector(".pop").classList.remove("active");
    });
/*popup2 js*/
    document.querySelector(" #bills").addEventListener("click",function (){
    document.querySelector(" .pop2 ").classList.add("active");
    });
    document.querySelector(".close-btn2").addEventListener("click",function (){
    document.querySelector(".pop2").classList.remove("active");
    });
/*popup3 js*/
    document.querySelector(" #paid ").addEventListener("click",function (){
    document.querySelector(" .pop3 ").classList.add("active");
    });
    document.querySelector(".close-btn").addEventListener("click",function (){
    document.querySelector(".pop3").classList.remove("active");
    });