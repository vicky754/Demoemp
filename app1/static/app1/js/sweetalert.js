/*$("#mybutton").click(function(){
	var name = $ ("#name").val();
	var email = $ ("#email").val();
	var password = $ ("#password").val();

	if (name == '' || email == '' || password == ''){
		alert("Please check the missing Field")
	}

})*/

/*
function popUp() {
	
	swal("Good job!", "User create Successfully!", "success");
}*/


const form =document.getElementById("form");
const username =document.getElementById("username");
const email =document.getElementById("email");
const password =document.getElementById("password");

//add event
/*
form.addEventListener('submit',(event) => {
	event.preventDefault();
	validate();
})*/





const sendData = (successRate,count) => {
	if (successRate === count ){
		swal("Good job!", "Registration Successfully!", "success");
		//location.href = `signup.html`
		location.replace = `signup.html`
	}
}


//for final dada validation
const successMsg = () => {
	let formCon = document.getElementsByClassName("form-control");
	var count= formCon.length - 1;
	for (var i=0 ; i< formCon.length; i++){
		if ( formCon[i].className === "form-control success"){
			var successRate = 0 + i;
			console.log(successRate);
			sendData(successRate,count);
		}else{
			return false;
		}
	}
}

//more email validate
/*const isEmail = (emailVal) => {
	var atSymbol = emailVal.indexOf("@");
	if(atSymbol < 1)return false;
	var dot = emailVal.lastIndexOf(".");
	if(dot <= atSymbol + 2) return false;
	if(dot == emailVal.length-1) return false;
	return true

}*/

//define the validate function
const validate = () => {
	const usernameVal = username.value.trim();
	const emailVal = email.value.trim();
	const passwordVal = password.value.trim();

	//validate username
	if(usernameVal === ""){
		setErrorMsg(username,'username cannot be blank');
	}else if(usernameVal.length <= 2){
		setErrorMsg(username,'username min 3 char');
	}else{
		setSuccessMsg(username);
	}

	//validate email
	if(emailVal === ""){
		setErrorMsg(email,'email cannot be blank');
	}else{
		setSuccessMsg(email);
	}

	//validate password
	if(passwordVal === ""){
		setErrorMsg(password,'password cannot be blank');
	}else if(passwordVal.length <= 5){
		setErrorMsg(password,'Minimum 6 char');
	}else{
		setSuccessMsg(password);
	}	

	successMsg();

}

function setErrorMsg(input,errormsgs){
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className ="form-control error";
	small.innerText = errormsgs;	
}

function setSuccessMsg(input){
	const formControl = input.parentElement;
	formControl.className ="form-control success";	
}

