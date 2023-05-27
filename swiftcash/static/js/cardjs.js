const cardNumber = document.getElementById("number");
const numberInp = document.getElementById("card_number");

const cardName = document.getElementById("name");
const nameInp = document.getElementById("card_name");

const cardMonth = document.getElementById("month");
const monthInp = document.getElementById("card_month");

const cardYear = document.getElementById("year");
const yearInp = document.getElementById("card_year");

const cardCvv = document.getElementById("cvv");
const cvvInp = document.getElementById("card_cvv");

const form = document.querySelector("form");

function setCardNumber(e)
{
cardNumber.innerText = format(e.target.value);
}

function setCardName(e)
{
cardName.innerText =  format(e.target.value);
}

function setCardMonth(e)
{
cardMonth.innerText =  format(e.target.value);
}

function setCardYear(e)
{
cardYear.innerText = format(e.target.value);
}

function setCardCvv(e)
{
cardCvv.innerText =  format(e.target.value);
}

function handlesubmit(e)
{
	e.preventDefault();
	if (!nameInp.value)
	{
		nameInp.classList.add("error");
		nameInp.parentElement.classList.add("error_message");
	}
	else
	{
		nameInp.classList.remove("error");
		nameInp.parentElement.classList.remove("error_message");
	}

	if (!numberInp.value)
	{
		numberInp.classList.add("error");
		numberInp.parentElement.classList.add("error_message");
	}
	else
	{
		numberInp.classList.remove("error");
		numberInp.parentElement.classList.remove("error_message");
	}

	if (!monthInp.value)
	{
		monthInp.classList.add("error");
		monthInp.parentElement.classList.add("error_message");
	}
	else
	{
		monthInp.classList.remove("error");
		monthInp.parentElement.classList.remove("error_message");
	}

	if (!yearInp.value)
	{
		yearInp.classList.add("error");
		yearnp.parentElement.classList.add("error_message");
	}
	else
	{
		yearInp.classList.remove("error");
		yearInp.parentElement.classList.remove("error_message");
	}

	if (!cvvInp.value)
	{
		cvvInp.classList.add("error");
		cvvInp.parentElement.classList.add("error_message");
	}
	else
	{
		cvvInp.classList.remove("error");
		cvvInp.parentElement.classList.remove("error_message");
	}
	if(nameInp.value && numberInp.value && monthInp.value && yearInp.value && cvvInp.value){
	return true;
	}

	
}

function format(s)
{
return s.toString().replace(/\d{4}(?=.)/g, "$& ");
}

numberInp.addEventListener("keyup",setCardNumber);
nameInp.addEventListener("keyup",setCardName);
monthInp.addEventListener("keyup",setCardMonth);
yearInp.addEventListener("keyup",setCardYear);
cvvInp.addEventListener("keyup",setCardCvv);
submitBtn.addEventListener("click",handlesubmit);