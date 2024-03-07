from django.contrib import admin
from django.urls import path,include
from . import views
admin_url = "saAm"
super_admin_url = "SAam"

urlpatterns = [
    path('', views.index , name = "index"),
    # path('signup/',views.signup),
    # path('index/',views.index,name="index"),
    path('login/',views.dashboard_login_merchant,name="dashboard-login-merchant"),
    path('my_wallet/',views.my_wallet,name='my_wallet'),



    path('login-{admin_url}/'.format(admin_url=admin_url),views.dashboard_login_admin,name="dashboard-login-Admin"),
    path('payout-merchants' , views.payout_merchants ,name= "payout-merchants"),
    path('payout-transaction' , views.payout_transaction ,name= "payout-transaction"),
    path('request-table' , views.request_table ,name= "request-table"),
    # path('login-saAm/',views.dashboard_login_admin,name="dashboard-login-Admin"),
    
    path('login-{super_admin_url}/'.format(super_admin_url=super_admin_url),views.dashboard_login_super_admin,name="dashboard-login-Super-Admin"),
    path('logout/',views.logout,name="user-logout"),
    path('add-admin/',views.add_admin,name = "add-admin"),
    path('edit-admin/<str:empid>/',views.edit_admin,name = "edit_admin"),
    path('view-admin/',views.view_admin,name="view-admin"),
    path('view-session/',views.view_session,name="view-session"),
    path('add-merchant/',views.add_merchant,name="add-merchant"),
    path('view-merchant/',views.view_merchant,name="view-merchant"),
    path('active-merchant/',views.active_merchant,name="active-merchant"),
    path('edit-merchant/<str:merchid>/',views.edit_merchant, name = "edit_merchant"),
    path('merchant-status/',views.merchant_status,name='merchant_status'),
    path('ip-update/',views.merchant_ip,name='merchant_ip'),

    
    # path('index-2/',views.index2,name="index-2"),
    
    path('invoices/',views.invoices,name="invoices"),
    path('cards-center/',views.cards_center,name="cards-center"),
    path('transactions/',views.transactions,name="transactions"),

    path('transactions-details/',views.transactions_details,name="transactions-details"),
  
    path('app-profile/',views.app_profile,name="app-profile"),
    path('post-details/',views.post_details,name="post-details"),
    path('email-compose/',views.email_compose,name="email-compose"),
    path('email-inbox/',views.email_inbox,name="email-inbox"),
    path('email-read/',views.email_read,name="email-read"),
    path('app-calender/',views.app_calender,name="app-calender"),
    path('ecom-product-grid/',views.ecom_product_grid,name="ecom-product-grid"),
    path('ecom-product-list/',views.ecom_product_list,name="ecom-product-list"),
    path('ecom-product-detail/',views.ecom_product_detail,name="ecom-product-detail"),
    path('ecom-product-order/',views.ecom_product_order,name="ecom-product-order"),
    path('ecom-checkout/',views.ecom_checkout,name="ecom-checkout"),
    path('ecom-invoice/',views.ecom_invoice,name="ecom-invoice"),
    path('ecom-customers/',views.ecom_customers,name="ecom-customers"),
    path('chart-flot/',views.chart_flot,name="chart-flot"),
    path('chart-morris/',views.chart_morris,name="chart-morris"),
    path('chart-chartjs/',views.chart_chartjs,name="chart-chartjs"),
    path('chart-chartist/',views.chart_chartist,name="chart-chartist"),
    path('chart-sparkline/',views.chart_sparkline,name="chart-sparkline"),
    path('chart-peity/',views.chart_peity,name="chart-peity"),

    path('ui-accordion/',views.ui_accordion,name="ui-accordion"),
    path('ui-alert/',views.ui_alert,name="ui-alert"),
    path('ui-badge/',views.ui_badge,name="ui-badge"),
    path('ui-button/',views.ui_button,name="ui-button"),
    path('ui-modal/',views.ui_modal,name="ui-modal"),
    path('ui-button-group/',views.ui_button_group,name="ui-button-group"),
    path('ui-list-group/',views.ui_list_group,name="ui-list-group"),
    path('ui-media-object/',views.ui_media_object,name="ui-media-object"),
    path('ui-card/',views.ui_card,name="ui-card"),
    path('ui-carousel/',views.ui_carousel,name="ui-carousel"),
    path('ui-dropdown/',views.ui_dropdown,name="ui-dropdown"),
    path('ui-popover/',views.ui_popover,name="ui-popover"),
    path('ui-progressbar/',views.ui_progressbar,name="ui-progressbar"),
    path('ui-tab/',views.ui_tab,name="ui-tab"),
    path('ui-typography/',views.ui_typography,name="ui-typography"),
    path('ui-pagination/',views.ui_pagination,name="ui-pagination"),
    path('ui-grid/',views.ui_grid,name="ui-grid"),

    path('uc-select2/',views.uc_select2,name="uc-select2"),
    path('uc-nestable/',views.uc_nestable,name="uc-nestable"),
    path('uc-noui-slider/',views.uc_noui_slider,name="uc-noui-slider"),
    path('uc-sweetalert/',views.uc_sweetalert,name="uc-sweetalert"),
    path('uc-toastr/',views.uc_toastr,name="uc-toastr"),
    path('map-jqvmap/',views.map_jqvmap,name="map-jqvmap"),
    path('uc-lightgallery/',views.uc_lightgallery,name="uc-lightgallery"),
    path('uc-lightgallery/',views.uc_lightgallery,name="uc-lightgallery"),
    path('widget-basic/',views.widget_basic,name="widget-basic"),

    path('form-element/',views.form_element,name="form-element"),
    path('form-wizard/',views.form_wizard,name="form-wizard"),
    path('form-ckeditor/',views.form_ckeditor,name="form-ckeditor"),
    path('form-pickers/',views.form_pickers,name="form-pickers"),
    path('form-validation-jquery/',views.form_validation_jquery,name="form-validation-jquery"),
    path('refresh/',views.refresh_jwt,name="refresh"),

    path('table-bootstrap-basic/',views.table_bootstrap_basic,name="table-bootstrap-basic"),
    path('table-datatable-basic/',views.table_datatable_basic,name="table-datatable-basic"),
# login and user creation
   
    path('page-register/',views.page_register,name="page-register"),
    path('page-forgot-password/',views.page_forgot_password,name="page-forgot-password"),
    path('page-lock-screen/',views.page_lock_screen,name="page-lock-screen"),
    path('page-error-400/',views.page_error_400,name="page-error-400"),
    path('page-error-403/',views.page_error_403,name="page-error-403"),
    path('page-error-404/',views.page_error_404,name="page-error-404"),
    path('page-error-500/',views.page_error_500,name="page-error-500"),
    path('page-error-503/',views.page_error_503,name="page-error-503"),
]