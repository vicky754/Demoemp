from django.shortcuts import render,redirect
from app1.models import Employee
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout
from django.views.generic import *
from .resources import EmployeeResource
from django.contrib import messages
from django.http import HttpResponse
from tablib import Dataset
import xlwt
import datetime
from django.http import HttpResponse
import csv
from .forms import *

# Create your views here.

# def empsearch(request):
#     query=request.GET['query']
#     q=Employee.objects.filter(name__icontains=query)
#     return render(request,'emplist.html',{'emp':q})

def simple_upload(request):
	if request.method == 'POST':
		employee_resource = EmployeeResource()
		dataset = Dataset()
		new_emp=request.FILES['file']

		if not new_emp.name.endswith('xlsx'):
			messages.info(request,'WRONG FORMAT')
			return render(request,'upload.html')

		
	
		imported_data = dataset.load(new_emp.read(),format='xlsx')
		for data in imported_data:
			value= 	Employee(
					data[0],
					data[1],
					data[2],
					data[3],
					data[4],
					data[5],
					data[6],
					data[7],
					data[8],
					data[9],
					)
		
			value.save()
	return render(request,'upload.html')

				


def home(request):
	return render(request,'home.html')


def login(request):
	if(request.method == 'GET'):
		return render(request,'login.html')

	else:
		name=request.POST.get('name')
		password=request.POST.get('password')

		try:
			user=Employee.objects.get(name=name)
			flag = check_password(password=password,encoded=user.password)
			if flag:
				temp={}
				temp['name']=user.name
				temp['id']=user.id
				request.session['user']=temp
				return redirect('home')
			else:
				return render(request,'login.html',{'error' :' Email or Password Invalid'})
			
		except:
			return render(request,'login.html',{'error' :' Email or Password Invalid'})


	

def signup(request):
	if(request.method == 'POST'):
		try:
			name=request.POST.get('name')
			date_of_birth=request.POST.get('date_of_birth')
			date_of_joining=request.POST.get('date_of_joining')
			gender=request.POST.get('gender')
			designation=request.POST.get('designation')
			reporting_manager=request.POST.get('reporting_manager')
			emp_image=request.POST.get('emp_image')
			password=request.POST.get('password')
			hashedpassword=make_password(password=password)
			email=request.POST.get('email')
			emp=Employee(name=name,date_of_birth=date_of_birth,date_of_joining=date_of_joining,gender=gender,designation=designation,reporting_manager=reporting_manager,emp_image=emp_image,password=hashedpassword,email=email)
			result=emp.save()
			return redirect('login')
		except:
			return render(request,'signup.html')

	return render(request,'signup.html')


def signout(request):
	request.session.clear()
	return redirect('home')


def emplist(request):
	header="List of Employee"
	form=EmployeeSearchForm(request.POST or None)
	emp=Employee.objects.all()
	context={
		
		'emp':emp,
		'form':form
	}
	
	if request.method=='POST':
		emp=Employee.objects.filter(name__icontains=form['name'].value())
		if form['export_to_CSV'].value()==True:
			response=HttpResponse(content_type='text/csv')
			response['Content-Disposition'] = 'attachment; filename="List of employee.csv"'
			writer = csv.writer(response)
			writer.writerow(['NAME', 'DATE OF BIRTH', 'DATE OF JOINING','GENDER','DESIGNATION','REPORTING MANAGER','EMAIL'])
			instance = emp
			for x in instance:
			 writer.writerow([x.name, x.date_of_birth, x.date_of_joining,x.gender,x.designation,x.reporting_manager,x.email])
			return response
		context={
		
		'emp':emp,
		'form':form
				}
	return render(request,'emplist.html',context)


def empdelete(request,id):
	emp=Employee.objects.get(id=id)
	emp.delete()
	return redirect("emplist")


class empedit(UpdateView):

    model=Employee
    template_name='empedit.html'
    fields=['name','date_of_birth','date_of_joining','gender','designation','reporting_manager','emp_image','email']
    success_url='/emplist/'




def export_excel(request):
	form=EmployeeSearchForm(request.POST or None)
	response =HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition']='attachment; filename=Userdata'+ str(datetime.datetime.now()) +'.xls'

	wb=xlwt.Workbook(encoding='utf-8')
	ws=wb.add_sheet('Employee data')

	row_num = 0

	font_style=xlwt.XFStyle()
	font_style.font.bold=True


	columns=['name','date_of_birth','date_of_joining','gender','designation','reporting_manager','email']

	for col_num in range(len(columns)):
		ws.write(row_num,col_num,columns[col_num],font_style)

	font_style=xlwt.XFStyle()

	
#name__icontains=form['name'])
	rows =Employee.objects.all().values_list('name','date_of_birth','date_of_joining','gender','designation','reporting_manager','email')

	for row in rows:
		row_num += 1

		for col_num in range(len(row)):
			ws.write(row_num,col_num,str(row[col_num]),font_style)
	wb.save(response)

	return response