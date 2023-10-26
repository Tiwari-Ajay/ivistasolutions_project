from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from SystemUser.views import *
urlpatterns = [
    path("superuser/",superuser,name="superuser"),
    path("registrationbydistiller/",RegistrationByDistiller,name="registrationbydistiller"),
    path("registrationbydistributor/",RegistrationByDistributor,name="registrationbydistributor"),
    path("index/",index,name="index"),
    path("distiller/",distiller,name="distiller"),
    path("distributor/",distributor,name="distributor"),
    path("retailor/",retailor,name="retailor"),
    path("saveregistration/",saveRegistration,name='saveregistration'),
    path("",userLogin,name="userlogin"),
    path("verifyregistration/",verify_Registration,name="verifyregistration"),
    path("dataloading/",dataLoading, name="dataloading"),
    path("usermanagementadmindistiller/",userManagementAdminDistiller, name="usermanagementadmindistiller"),
    path("usermanagementdistributorretailor/",userManagementDistributorRetailor, name="usermanagementdistributorretailor"),
    path("distillerwise_analysis/",distillerwise_analysis, name="distillerwise_analysis"),
    #new added
    path("image_view/<str:email_id>/",image_view,name='image_view'),
    path("verifyRegistration/",verifyRegistration,name="verifyRegistration"),
    path("saveVerifiedRegistration<str:profile>/",saveVerifiedRegistration,name='saveVerifiedRegistration'),
    path("deleteRegistration<str:email_id>/",deleteRegistration,name='deleteRegistration'),
    path("datatable_admin_view_distiller/",datatable_admin_view_distiller,name='datatable_admin_view_distiller'), #to view admin
    path("datatable_admin_view_distributor/",datatable_admin_view_distributor,name='datatable_admin_view_distributor'), #to view admin
    path("datatable_admin_view_retailor/",datatable_admin_view_retailor,name='datatable_admin_view_retailor'), #to view admin
    path("available_stock/",available_stock,name='available_stock'), #to view for admin
    path("product_details/",product_details,name='product_details'), #to view for admin
    path("admin_distillerwise_analysis/",admin_distillerwise_analysis,name='admin_distillerwise_analysis'), #to view for admin
    path("map_admin_show_distiller/",map_admin_show_distiller,name='map_admin_show_distiller'), #to view for admin
    path("admin_report_generation/",admin_report_generation,name='admin_report_generation'), #to view for admin
    path("server_page/",server_page,name='server_page'), #server for distiller
    path("client_page/",client_page,name='client_page'), #client for distiller
    path("tkinter_server_run/",tkinter_server_run,name='tkinter_server_run'),


]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
