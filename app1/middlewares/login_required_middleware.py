from django.shortcuts import render,redirect



def login_required(get_response):
	def middleware(request):
		user=request.session.get('user')
		if user:

			#print("middleware")
			response = get_response(request)
			return response
		else:
			#print("please login")
			return redirect('login')
	return middleware