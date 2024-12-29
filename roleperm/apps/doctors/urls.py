

from django.urls import path
from . import views


urlpatterns = [
    path("doc_listing/",views.listing_doc,name="doc_listing")
]