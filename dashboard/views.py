import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required 

import datetime
from .forms import *
import requests
# for i in range(0,10000):

#     

#@login_required(login_url='dashboard:login')


def index(request):

    print(request.session.get('jwt_token'))
    context={
        "page_title":"Dashboard"
    }
    return render(request,'dashboard/index-2.html',context)


def page_login(request):

    if request.method == "POST":
        data = {
            "email": request.POST.get("email"),
            "password": request.POST.get("password")
        }

        url = "http://192.168.1.6:8000/login/"
        response = requests.post(url, data=data)
        slug = response.headers
        print(slug)


        jwt_token_access = response.headers['access']
        jwt_token_refresh = response.headers['refresh']
        user_data = response.json()

        # Store user data in session
        request.session['jwt_token_access'] = jwt_token_access
        request.session['jwt_token_refresh'] = jwt_token_refresh
        
        request.session['user_data'] = user_data
        return redirect ("/", request ,slug)


    form = LoginForm
    return render(request,'dashboard/modules/login.html',{"form":form})


def add_admin(request):

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
            "ip_address": "192.168.1.9.1",
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

        url = "http://192.168.1.6:8000/register-admin/"
        response = requests.post(url, data=data2 , headers=header)
        slug = response.json()
        print(slug)

    form = AdminForm
    context={
        "page_title":"Signup",
        "form":form,
    }

    return render (request,'dashboard/admin/add-admin.html',context)


def view_admin(request):

    return render (request, 'dashboard/admin/view-admin.html')

def view_merchant(request):

    return render (request , 'dashboard/merchant/view_merchant.html')

def add_merchant(request):

    return render  (request,'dashboard/merchant/view_merchant.html')
def logout(request):
    # Remove JWT token and user data from the session
    if 'jwt_token' in request.session:
        del request.session['jwt_token']

    if 'user_data' in request.session:
        del request.session['user_data']


    return redirect ("page_login")


def refresh_jwt(request):
    access_token = request.session.get('jwt_token_access')
    refresh_token = request.session.get('jwt_token_refresh')
    url = "http://192.168.1.6:8000/token/refresh/"

    token = {
            "refresh":refresh_token,
            
        }
    response = requests.post(url, data=token)

    user_data = response.json()

    print(type(user_data),user_data)
    user_data = json.loads(user_data)
    print(type(user_data),user_data)
    
    jwt_token_access = user_data['access']
    jwt_token_refresh = user_data['refresh']
    # Store user data in session
    request.session['jwt_token_access'] = jwt_token_access
    request.session['jwt_token_refresh'] = jwt_token_refresh
        
    



#@login_required(login_url='dashboard:login')
def my_wallet(request):
    context={
        "page_title":"My Wallet"
    }
    return render(request,'dashboard/my-wallet.html',context)

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



