from django.shortcuts import render

# Create your views here.

def listing_doc(request):
    return render(request,"doc_listing.html")