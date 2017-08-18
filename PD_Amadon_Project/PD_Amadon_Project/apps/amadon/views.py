# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from products import items

def index(request):
    
    context = {
        "items": items
    }
    
    return render(request, "amadon/index.html", context)

def buy(request, item_id):
    
    try:
        request.session['current_charge'] = ""
    except:
        request.session['current_charge'] = ""

    try:
        request.session['total_items']
    except:
        request.session['total_items'] = 0

    try:
        request.session['total_charges']
    except:
        request.session['total_charges'] = 0

    
    current_charge = 0
    quantity = int(request.POST.get('quantity'))
    for item in items:
        if item['id'] == int(item_id):
            current_charge = item['price'] * quantity
    
    request.session['current_charge'] = str(current_charge)
    
    request.session['total_items'] = int(request.session['total_items']) + quantity
    request.session['total_charges'] = int(request.session['total_charges']) + current_charge
    
    request.session.modified = True
    print "Current Charge: {}".format(request.session['current_charge'])
    print "Total Items: {}".format(request.session['total_items'])
    print "Total Charges: {}".format(request.session['total_charges'])
    return redirect('/checkout')
    
def checkout(request):
    
    return render(request, "amadon/checkout.html")