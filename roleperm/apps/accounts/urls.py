from . import views
from django.urls import path

urlpatterns = [
    path("product_list/",views.product_list,name="product_list"),
    path("admin_dashboard/",views.admin_dashboard,name="admin_dashboard"),
]