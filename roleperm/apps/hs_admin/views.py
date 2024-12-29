from django.shortcuts import render

from apps.accounts.decorator import allowed_users

# Create your views here.
@allowed_users(allowed_roles=['Admin'])
def admin_dashboard(request):
    return render(request,"admin_dashboard.html")