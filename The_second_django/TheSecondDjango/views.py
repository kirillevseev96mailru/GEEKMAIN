from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Products, Orders, Clients
from datetime import date, datetime


def index(request):
    return render(request, 'TheSecondDjango/index.html')


def about(request):
    return render(request, 'TheSecondDjango/about.html')


def all_the_time(request, name):
    client = get_object_or_404(Clients, name=name)
    orders = get_list_or_404(Orders, name_client=client.id)
    new_orders = []
    for order in orders:
        d0 = date(date.today().year, date.today().month, date.today().day)
        d1 = date(order.date.year, order.date.month, order.date.day)
        delta = d0 - d1
        new_orders.append([order, delta.days])
    return render(request, 'TheSecondDjango/all_the_time.html', {
        'orders': new_orders,
        'client': client,
    })
