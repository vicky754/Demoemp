
from django.urls import path
from .views import *
from app1.middlewares.login_required_middleware import login_required
from app1.middlewares.cannot_access_after_login import cannotAaccessAfterLogin

urlpatterns = [
    
    path('',login_required(home),name='home'),
    path('login/',cannotAaccessAfterLogin(login),name='login'),
    path('signup/',cannotAaccessAfterLogin(signup)),
    path('logout/',signout,name='logout'),
    path('emplist/',login_required(emplist),name='emplist'),
    path('empdelete/<int:id>/',(empdelete)),
    path('empedit/<int:pk>/',(empedit.as_view())),
    path('simple_upload/',login_required(simple_upload)),
    #path('empsearch/',login_required(empsearch)),
    #path('success/',success),
    path('export_excel/',login_required(export_excel),name='export-excel')


]