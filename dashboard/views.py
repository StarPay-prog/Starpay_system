import json
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required, permission_required 
from .models import *

import datetime
from .forms import *
import requests
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from .authentication import *
# for i in range(0,10000):
from starpay.settings import base_url,payout_url
     

#@login_required(login_url='dashboard:login')


def index(request):
    # refresh_jwt(request)

    print(request.session.get('jwt_token'))
    

    user_type = request.session.get('user_type')
    
    context={
        "page_title":"Dashboard",
        "type": user_type
    }
    return render(request,'dashboard/index.html',context)

def dashboard_login_merchant(request):

    if request.method == "POST":
        data = {
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
            "user_type":777
        }

        url = base_url + "login/"
        response = requests.post(url, data=data)
        
        jwt_token_access = response.headers['access']
        jwt_token_refresh = response.headers['refresh']
        user_data = response.json()
        user = user_data['data']
        usertype = "merchant"
        request.session['user_type'] = usertype
        print(usertype)
        user_ip = request.META.get('REMOTE_ADDR')
        forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded_for:
            user_ip = forwarded_for.split(',')[0].strip()


        # Store user data in session
        request.session['jwt_token_access'] = jwt_token_access
        request.session['jwt_token_refresh'] = jwt_token_refresh
        
        request.session['user_data'] = user_data
        request.session['ip'] = user_ip
        request.session['user_type'] = "merchant"
        session_key = request.session.session_key
        print(session_key)
        # try:
        #     # Retrieve the Session instance corresponding to the session key
        #     session_instance = Session.objects.get(session_key=session_key)
        # except Session.DoesNotExist:
        #     # Handle the case where the session does not exist
        #     return HttpResponse("Session does not exist")
    

       #  Custom Session management is to be done here no cutom session is created
        
        # CustomSession.objects.create(session = session_instance ,
        #                              IP = user_ip,
        #                              user = "aaa",
        #                              user_type = usertype )
        
        return redirect ("/", request )


    form = LoginForm
    return render(request,'dashboard/modules/login.html',{"form":form})

def dashboard_login_admin(request):

    if request.method == "POST":
        data = {
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
            "user_type":888
        }

        url = base_url + "login/"
        response = requests.post(url, data=data)
        print(response)
        jwt_token_access = response.headers['access']
        jwt_token_refresh = response.headers['refresh']
        user_data = response.json()
        print(user_data)
        user = user_data['data']
        usertype = "admin"
       
        request.session['user_type'] = usertype
        print(usertype)

        user_ip = request.META.get('REMOTE_ADDR')
    
   
        forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded_for:
            user_ip = forwarded_for.split(',')[0].strip()


        # Store user data in session
        request.session['jwt_token_access'] = jwt_token_access
        request.session['jwt_token_refresh'] = jwt_token_refresh
        
        request.session['user_data'] = user
        request.session['ip'] = user_ip
        request.session['user_type'] = "admin"
        session_key = request.session.session_key

        print(request.session ,session_key) 
        try:
            # Retrieve the Session instance corresponding to the session key
            session_instance = Session.objects.get(session_key=session_key)
        except Session.DoesNotExist:
            # Handle the case where the session does not exist
            return HttpResponse("Session does not exist")
    

       #  Custom Session management is to be done here no cutom session is created
        
        # CustomSession.objects.create(session = session_instance ,
        #                              IP = user_ip,
        #                              user = "aaa",
        #                              user_type = usertype )
        return redirect ("/", request )


    form = LoginForm
    return render(request,'dashboard/modules/login.html',{"form":form})

def payout_merchants(request):

    return render (request , 'dashboard/admin/payout-merchant.html',)


def request_table(request):

    return render (request , 'dashboard/admin/request-table.html',)

def payout_transaction(request):

    return render (request , 'dashboard/admin/payout-transaction.html',)

def api_logs(request):

    return render (request , 'dashboard/admin/api-logs.html',)

def dashboard_login_super_admin(request):

    if request.method == "POST":
        data = {
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
            "user_type":999
        }

        url = base_url + "login/"
        response = requests.post(url, data=data)
        
        jwt_token_access = response.headers['access']
        jwt_token_refresh = response.headers['refresh']
        user_data = response.json()
        print(user_data)

        user = user_data['data']
        usertype = "super_admin"
        request.session['user_type'] = usertype

        user_ip = request.META.get('REMOTE_ADDR')
    
   
        forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded_for:
            user_ip = forwarded_for.split(',')[0].strip()


        # Store user data in session
        request.session['jwt_token_access'] = jwt_token_access
        request.session['jwt_token_refresh'] = jwt_token_refresh
        
        request.session['user_data'] = user_data
        request.session['ip'] = user_ip
        request.session['user_type'] = "superadmin"
        

        print(request.session)
        session_key = request.session.session_key
        print(request.session.session_key)

        try:
            # Retrieve the Session instance corresponding to the session key
            session_instance = Session.objects.get(session_key=session_key)
            print(session_instance,"intance")
        except Session.DoesNotExist:
            # Handle the case where the session does not exist
            return HttpResponse("Session does not exist")
    
#  Custom Session management is to be done here no cutom session is created
        
        # CustomSession.objects.create(session = session_instance ,
        #                              IP = user_ip,
        #                              user = "aaa",
        #                              user_type = usertype )
        
        return redirect ("/", request )


    form = LoginForm
    return render(request,'dashboard/modules/login.html',{"form":form})



def add_admin(request):
    # refresh_jwt(request)

    if request.method == "POST":
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        print(first_name,last_name,email,phone_number,password)
        data2 = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "contact_no": phone_number,
            "ip_address": "192.168.1.13.1",
            "password" : password
        }
        
        data2 = json.dumps(data2)
        print(data2)
        # Define the JWT token
        jwt_token = request.session.get('jwt_token_access')
        # print(type(jwt_token))
        # jwt_token = jwt_token['access']

        # Define the headers with the JWT token
        header = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"  # Assuming you are sending JSON data
        }

        print(header)

        url = base_url + "register-admin/"
        response = requests.post(url, data=data2 , headers=header)
        slug = response.json()
        print(slug)
        slug = slug['status']
        form = AdminForm
        return render (request,'dashboard/admin/add-admin.html',{"response":slug, "form":form,} )


    form = AdminForm
    context={
        "page_title":"Signup",
        "form":form,
    }

    return render (request,'dashboard/admin/add-admin.html',context)


def view_admin(request):
    

    jwt_token = request.session.get('jwt_token_access')

    header = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"  # Assuming you are sending JSON data
        }


    url = "http://192.168.1.13:9000/get-admin-list/"

    response = requests.get(url, headers=header)

    response = response.json()

    print(response['data'])
    return render (request, 'dashboard/admin/view-admin.html',context = {"data":response['data']})

def view_session(request):

    return render (request, 'dashboard/admin/view-session.html')

def view_merchant(request):
    # refresh_jwt(request)

    jwt_token = request.session.get('jwt_token_access')

    header = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"  # Assuming you are sending JSON data
        }

    if request.session.get('user_type') == 'admin':
        
        url = "http://192.168.1.13:9000/get-merchant-list-admin/"

    elif request.session.get('user_type') == 'superadmin':
       
        url = "http://192.168.1.13:9000/get-merchant-list-super/"

    response = requests.get(url, headers=header)

    response = response.json()

    print(type(response['data']))
    

    return render (request , 'dashboard/merchant/view-merchant.html',context= {"data":response['data']})


def edit_merchant(request,merchid):
    url = base_url + "get-merchant/" + merchid
    
    jwt_token = request.session.get('jwt_token_access')

    header = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"  # Assuming you are sending JSON data
        }


    if request.method == "POST":

        return HttpResponseRedirect("view-merchant")
    form = LoginForm
    
    response = requests.get(url, headers=header)

    return render (request,"dashboard/merchant/edit-merchant.html" ,context = {"form":form,
                                                           'data': response})

def edit_admin(request,empid):          
    url = base_url + "get-admin/" + empid
    
    jwt_token = request.session.get('jwt_token_access')

    header = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"  # Assuming you are sending JSON data
        }


    if request.method == "POST":

        return HttpResponseRedirect("view-admin")
    form = LoginForm
    
    response = requests.get(url, headers=header)

    return render (request,"dashboard/admin/edit-admin.html" ,context = {"form":form,
                                                           'data': response})


def active_merchant(request):

    return render  (request,'dashboard/merchant/active-merchant.html')

def my_wallet(request):

    return render  (request,'dashboard/merchant-dashboard/my_wallet.html')

def my_settings(request):

    return render  (request,'dashboard/merchant-dashboard/settings.html')

def my_profile(request):

    return render  (request,'dashboard/merchant-dashboard/profile.html')

def add_merchant(request):

    #refresh_jwt(request)
    emp_id = request.session.get('user_data')
    print(emp_id)
    emp_id =emp_id['emp_id']

    if request.method == "POST":
        serviceoptn = [request.POST.get('field1'),request.POST.get('field2'),request.POST.get('field3'),request.POST.get('field4')]
        print(serviceoptn)
        serviceoptn = [optn for optn in serviceoptn if optn is not None]
        print(serviceoptn)
        
        data2 = {
            
            "email": request.POST.get('email'),
            "first_name": request.POST.get('first_name'),
            "last_name": request.POST.get('last_name'),
            "contact_no": request.POST.get('phone_no'),
            "password": request.POST.get('password'),
            "business_name":request.POST.get('business_name'),
            "gst_no":request.POST.get('gst_no'),
            "emp_id":emp_id,
            "service_option":serviceoptn
        
        }
        
        data2 = json.dumps(data2)
        print(data2)
        # Define the JWT token
        jwt_token = request.session.get('jwt_token_access')
        # print(type(jwt_token))
        # jwt_token = jwt_token['access']

        # Define the headers with the JWT token
        header = {
        "Authorization": f"Bearer {jwt_token}",

        "Content-Type": "application/json"  # Assuming you are sending JSON data
        }

        print(header)

        url = "http://192.168.1.13:9000/register-merchant/"
        response = requests.post(url, data=data2 , headers=header)
        slug = response.json()
        slug = slug['status']
        

    print(emp_id)

    return render  (request,'dashboard/merchant/add-merchant.html')

def logout(request):


    # return render  (request,'dashboard/plugins/uc-sweetalert.html')
    session_key = request.session.session_key
    
    # Delete the session using Django's session framework
    Session.objects.filter(session_key=session_key).delete()
    
    # Delete the corresponding CustomSession object
    CustomSession.objects.filter(session=session_key).delete()


    return HttpResponseRedirect ("/login/")


def refresh_jwt(request):

    access_token = request.session.get('jwt_token_access')
    refresh_token = request.session.get('jwt_token_refresh')
    url = "http://192.168.1.13:9000/token/refresh/"

    token = {
            "refresh":refresh_token,
            
        }
    response = requests.post(url, data=token)

    user_data = response.json()

    print("data",user_data)
    jwt_token_access = user_data['access']
    jwt_token_refresh = user_data['refresh']
    

    # Store user data in session
    request.session['jwt_token_access'] = jwt_token_access
    request.session['jwt_token_refresh'] = jwt_token_refresh
    
        
def payout_merchants(request):

    url = payout_url+'Rest/payout-get-merchant-list-admin/'
    url1 = base_url + 'get-merchant-list-admin/'
    print(url)

    jwt_token = request.session.get('jwt_token_access')
    header = {
        "Access": jwt_token,
        "Content-Type": "application/json"  # Assuming you are sending JSON data
        }
    
    header1 = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"  # Assuming you are sending JSON data
        }
    
    response1 = requests.get(url, headers=header)

    response2 = requests.get(url1, headers=header1)
    
    print(response1.json())
    slug1 = response1.json()
    slug2 = response2.json()

    for i in slug2['data']:
        for j in slug1['data']:
            if j['merchant_id'] == i['merchant_id']:
                i.update(j)

    
    print(slug2)

    print(type(slug2))
    context = {
        'data':slug2['data']
    }

    return render (request , 'dashboard/admin/payout-merchant.html',context)


def payout_transaction(request):

    return render (request , 'dashboard/admin/payout-transaction.html',)

# response for ajax is handeled from here







#@login_required(login_url='dashboard:login')
def invoices(request):
    context={
        "page_title":"Invoices"
    }
    return render(request,'dashboard/invoices.html',context)

#@login_required(login_url='dashboard:login')
def cards_center(request):
    context={
        "page_title":"Cards Center"
    }
    return render(request,'dashboard/cards-center.html',context)

#@login_required(login_url='dashboard:login')
def transactions(request):
    context={
        "page_title":"Transactions"
    }
    return render(request,'dashboard/transactions.html',context)


#@login_required(login_url='dashboard:login')
def transactions_details(request):
    context={
        "page_title":"Transactions Details"
    }
    return render(request,'dashboard/transactions-details.html',context)



#@login_required(login_url='dashboard:login')
def app_profile(request):
    context={
        "page_title":"Profile"
    }
    return render(request,'dashboard/apps/app-profile.html',context)


#@login_required(login_url='dashboard:login')
def post_details(request):
    context={
        "page_title":"Post Details"
    }
    return render(request,'dashboard/apps/post-details.html',context)

#@login_required(login_url='dashboard:login')
def email_compose(request):
    context={
        "page_title":"Compose"
    }
    return render(request,'dashboard/apps/email/email-compose.html',context)

#@login_required(login_url='dashboard:login')
def email_inbox(request):
    context={
        "page_title":"Inbox"
    }
    return render(request,'dashboard/apps/email/email-inbox.html',context)

#@login_required(login_url='dashboard:login')
def email_read(request):
    context={
        "page_title":"Read"
    }
    return render(request,'dashboard/apps/email/email-read.html',context)

#@login_required(login_url='dashboard:login')
def app_calender(request):
    context={
        "page_title":"Calendar"
    }
    return render(request,'dashboard/apps/app-calender.html',context)


#@login_required(login_url='dashboard:login')
def ecom_product_grid(request):
    context={
        "page_title":"Product-Grid"
    }
    return render(request,'dashboard/apps/shop/ecom-product-grid.html',context)

#@login_required(login_url='dashboard:login')
def ecom_product_list(request):
    context={
        "page_title":"Product-List"
    }
    return render(request,'dashboard/apps/shop/ecom-product-list.html',context)

#@login_required(login_url='dashboard:login')
def ecom_product_detail(request):
    context={
        "page_title":"Product-Detail"
    }
    return render(request,'dashboard/apps/shop/ecom-product-detail.html',context)

#@login_required(login_url='dashboard:login')
def ecom_product_order(request):
    context={
        "page_title":"Product-Order"
    }
    return render(request,'dashboard/apps/shop/ecom-product-order.html',context)

#@login_required(login_url='dashboard:login')
def ecom_checkout(request):
    context={
        "page_title":"Checkout"
    }
    return render(request,'dashboard/apps/shop/ecom-checkout.html',context)

#@login_required(login_url='dashboard:login')
def ecom_invoice(request):
    context={
        "page_title":"Invoice"
    }
    return render(request,'dashboard/apps/shop/ecom-invoice.html',context)

#@login_required(login_url='dashboard:login')
def ecom_customers(request):
    context={
        "page_title":"Customers"
    }
    return render(request,'dashboard/apps/shop/ecom-customers.html',context)


#@login_required(login_url='dashboard:login')
def chart_flot(request):
    context={
        "page_title":"Chart-Flot"
    }
    return render(request,'dashboard/charts/chart-flot.html',context)

#@login_required(login_url='dashboard:login')
def chart_morris(request):
    context={
        "page_title":"Chart-Morris"
    }
    return render(request,'dashboard/charts/chart-morris.html',context)

#@login_required(login_url='dashboard:login')
def chart_chartjs(request):
    context={
        "page_title":"Chart-Chartjs"
    }
    return render(request,'dashboard/charts/chart-chartjs.html',context)

#@login_required(login_url='dashboard:login')
def chart_chartist(request):
    context={
        "page_title":"Chart-Chartist"
    }
    return render(request,'dashboard/charts/chart-chartist.html',context)

#@login_required(login_url='dashboard:login')
def chart_sparkline(request):
    context={
        "page_title":"Chart-Sparkline"
    }
    return render(request,'dashboard/charts/chart-sparkline.html',context)

#@login_required(login_url='dashboard:login')
def chart_peity(request):
    context={
        "page_title":"Chart-Peity"
    }
    return render(request,'dashboard/charts/chart-peity.html',context)



#@login_required(login_url='dashboard:login')
def ui_accordion(request):
    context={
        "page_title":"Accordion"
    }
    return render(request,'dashboard/bootstrap/ui-accordion.html',context)

#@login_required(login_url='dashboard:login')
def ui_alert(request):
    context={
        "page_title":"Alert"
    }
    return render(request,'dashboard/bootstrap/ui-alert.html',context)

#@login_required(login_url='dashboard:login')
def ui_badge(request):
    context={
        "page_title":"Badge"
    }
    return render(request,'dashboard/bootstrap/ui-badge.html',context)

#@login_required(login_url='dashboard:login')
def ui_button(request):
    context={
        "page_title":"Button"
    }
    return render(request,'dashboard/bootstrap/ui-button.html',context)

#@login_required(login_url='dashboard:login')
def ui_modal(request):
    context={
        "page_title":"Modal"
    }
    return render(request,'dashboard/bootstrap/ui-modal.html',context)

#@login_required(login_url='dashboard:login')
def ui_button_group(request):
    context={
        "page_title":"Button Group"
    }
    return render(request,'dashboard/bootstrap/ui-button-group.html',context)

#@login_required(login_url='dashboard:login')
def ui_list_group(request):
    context={
        "page_title":"List Group"
    }
    return render(request,'dashboard/bootstrap/ui-list-group.html',context)

#@login_required(login_url='dashboard:login')
def ui_media_object(request):
    context={
        "page_title":"Media Object"
    }
    return render(request,'dashboard/bootstrap/ui-media-object.html',context)


#@login_required(login_url='dashboard:login')
def ui_card(request):
    context={
        "page_title":"Card"
    }
    return render(request,'dashboard/bootstrap/ui-card.html',context)


#@login_required(login_url='dashboard:login')
def ui_carousel(request):
    context={
        "page_title":"Carousel"
    }
    return render(request,'dashboard/bootstrap/ui-carousel.html',context)


#@login_required(login_url='dashboard:login')
def ui_dropdown(request):
    context={
        "page_title":"Dropdown"
    }
    return render(request,'dashboard/bootstrap/ui-dropdown.html',context)

#@login_required(login_url='dashboard:login')
def ui_popover(request):
    context={
        "page_title":"Popover"
    }
    return render(request,'dashboard/bootstrap/ui-popover.html',context)

#@login_required(login_url='dashboard:login')
def ui_progressbar(request):
    context={
        "page_title":"Progressbar"
    }
    return render(request,'dashboard/bootstrap/ui-progressbar.html',context)

#@login_required(login_url='dashboard:login')
def ui_tab(request):
    context={
        "page_title":"Tab"
    }
    return render(request,'dashboard/bootstrap/ui-tab.html',context)

#@login_required(login_url='dashboard:login')
def ui_typography(request):
    context={
        "page_title":"Typography"
    }
    return render(request,'dashboard/bootstrap/ui-typography.html',context)


#@login_required(login_url='dashboard:login')
def ui_pagination(request):
    context={
        "page_title":"Pagination"
    }
    return render(request,'dashboard/bootstrap/ui-pagination.html',context)
#@login_required(login_url='dashboard:login')
def ui_grid(request):
    context={
        "page_title":"Grid"
    }
    return render(request,'dashboard/bootstrap/ui-grid.html',context)




#@login_required(login_url='dashboard:login')
def uc_select2(request):
    context={
        "page_title":"Select"
    }
    return render(request,'dashboard/plugins/uc-select2.html',context)

#@login_required(login_url='dashboard:login')
def uc_nestable(request):
    context={
        "page_title":"Nestable"
    }
    return render(request,'dashboard/plugins/uc-nestable.html',context)

#@login_required(login_url='dashboard:login')
def uc_noui_slider(request):
    context={
        "page_title":"UI Slider"
    }
    return render(request,'dashboard/plugins/uc-noui-slider.html',context)


#@login_required(login_url='dashboard:login')
def uc_sweetalert(request):
    context={
        "page_title":"Sweet Alert"
    }
    return render(request,'dashboard/plugins/uc-sweetalert.html',context)

#@login_required(login_url='dashboard:login')
def uc_toastr(request):
    context={
        "page_title":"Toastr"
    }
    return render(request,'dashboard/plugins/uc-toastr.html',context)

#@login_required(login_url='dashboard:login')
def map_jqvmap(request):
    context={
        "page_title":"Jqvmap"
    }
    return render(request,'dashboard/plugins/map-jqvmap.html',context)

#@login_required(login_url='dashboard:login')
def uc_lightgallery(request):
    context={
        "page_title":"LightGallery"
    }
    return render(request,'dashboard/plugins/uc-lightgallery.html',context)

#@login_required(login_url='dashboard:login')
def widget_basic(request):
    context={
        "page_title":"Widget"
    }
    return render(request,'dashboard/widget-basic.html',context)

#@login_required(login_url='dashboard:login')
def form_element(request):
    context={
        "page_title":"Form Element"
    }
    return render(request,'dashboard/forms/form-element.html',context)

#@login_required(login_url='dashboard:login')
def form_wizard(request):
    context={
        "page_title":"Form Wizard"
    }
    return render(request,'dashboard/forms/form-wizard.html',context)

#@login_required(login_url='dashboard:login')
def form_ckeditor(request):
    context={
        "page_title":"Ckeditor"
    }
    return render(request,'dashboard/forms/form-ckeditor.html',context)

#@login_required(login_url='dashboard:login')
def form_pickers(request):
    context={
        "page_title":"Pickers"
    }
    return render(request,'dashboard/forms/form-pickers.html',context)


#@login_required(login_url='dashboard:login')
def form_validation_jquery(request):
    context={
        "page_title":"Form Validation"
    }
    return render(request,'dashboard/forms/form-validation-jquery.html',context)


#@login_required(login_url='dashboard:login')
def table_bootstrap_basic(request):
    context={
        "page_title":"Table Bootstrap"
    }
    return render(request,'dashboard/table/table-bootstrap-basic.html',context)

#@login_required(login_url='dashboard:login')
def table_datatable_basic(request):
    context={
        "page_title":"Table Datatable"
    }
    return render(request,'dashboard/table/table-datatable-basic.html',context)




#@login_required(login_url='dashboard:login')
def page_register(request):
    return render(request,'dashboard/pages/page-register.html')


#@login_required(login_url='dashboard:login')
def page_lock_screen(request):
    return render(request,'dashboard/pages/page-lock-screen.html')


#@login_required(login_url='dashboard:login')
def page_forgot_password(request):
    return render(request,'dashboard/pages/page-forgot-password.html')


def page_error_400(request):
    return render(request,'400.html')
    
def page_error_403(request):
    return render(request,'403.html')

def page_error_404(request):
    return render(request,'404.html')

def page_error_500(request):
    return render(request,'500.html')

def page_error_503(request):
    return render(request,'503.html')



