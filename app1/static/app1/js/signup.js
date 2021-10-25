/*function validate(event) {
	console.log("Form Submission")
		var error=document.getElementById('message')
			error.hidden=false
		console.log(error)
		var message=null
		var values = event.target.elements;
		var name =values.name.value;
		var email =values.email.value;
		var password =values.password.value;
		// var repassword =values.repassword.value;

		if (!name.trim()){
			message ="Name is required"
		}else if(!email.trim()){
			message="Email is required"
		}else if(!password.trim()){
			message="password is required"
		}
		else if(password.trim() != repassword.trim()){
			message="password not matched"
		}


		if(message){
			error=innerHTML=message
			error.hidden =false
		}else{
			error.innerHTML=''
			error.hidden=true
		}


		console.log({
			name,email,password
		})
	event.stopPropagation();
	return false
}










