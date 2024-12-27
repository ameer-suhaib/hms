from django.shortcuts import render
from . models import *

# Create your views here.


def home(request):
    customers = Customers.objects.all()
    orders = Orders.objects.all()
    customer_count = customers.count()
    order_count = orders.count()

    context = {"customers":customers,"orders":orders,"customer_count":customer_count,"order_count":order_count}
    return render(request,"dashborad.html",{"context":context})


def product_list(request):
    products = Products.objects.all()

    return render(request,"product_list.html",{"products":products})


def admin_dashboard(request):
    # Get counts for statistics cards
    total_customers = Customers.objects.count()
    total_products = Products.objects.count()
    total_orders = Orders.objects.count()
    
    # Calculate total revenue from orders
    total_revenue = sum(order.product.price for order in Orders.objects.select_related('product').all())

    # Get recent activities (orders)
    recent_activities = []
    recent_orders = Orders.objects.select_related('customer', 'product').order_by('-created_at')[:10]
    
    for order in recent_orders:
        status_color = {
            'Pending': 'warning',
            'Out of Delivary': 'info',
            'Delivered': 'success'
        }.get(order.status, 'secondary')

        recent_activities.append({
            'timestamp': order.created_at,
            'description': f'Order placed for {order.product.name}',
            'user': order.customer.name,
            'status': order.status,
            'status_color': status_color
        })

    context = {
        'total_customers': total_customers,
        'total_products': total_products,
        'total_orders': total_orders,
        'total_revenue': "{:.2f}".format(total_revenue),
        'recent_activities': recent_activities,
    }

    return render(request, "admin_dashboard.html", context)
