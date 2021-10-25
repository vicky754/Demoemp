from django.contrib import admin
from app1.models import Employee
from import_export.admin import ImportExportModelAdmin


# class EmpAdmin(ImportExportModelAdmin):
# 	list_display= ['name','email']

class EmployeeAdmin(ImportExportModelAdmin):
	list_display = ['name','date_of_birth','date_of_joining','gender','designation','reporting_manager','emp_image','password','email']


admin.site.register(Employee,EmployeeAdmin)
#admin.site.register(Employee,EmpAdmin)