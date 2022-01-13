from django.http.response import HttpResponse
from django.shortcuts import render, redirect
import random, pytz
from datetime import datetime
from pytz import timezone

def index(request):
    if 'gold' not in request.session or 'activities' not in request.session or 'history' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = 0
        request.session['history'] = []
    context = {
        'history': request.session['history']
    }
    return render(request, 'index.html', context)

def process_money(request):
    if request.method == 'POST':
        total_amount = request.session['activities']
        location = request.POST['location']
        history = request.session['history']
        if location == 'farm':
            current_amount = round(random.random() * 10 + 10)
            total_amount += current_amount
            request.session['gold'] += current_amount
            request.session['activities'] = total_amount
            request.session['location'] = 'farm'
            date_format='%m/%d/%Y %H:%M:%S %Z'
            date = datetime.now(tz=pytz.utc)
            date = date.astimezone(timezone('US/Pacific'))
            myTime = date.strftime(date_format)
            print(myTime)
            str = f"Earned {current_amount} gold from the {location} at {myTime}."
            history.append(str)
            request.session['history'] = history
        if location == 'cave':
            current_amount = round(random.random() * 5 + 5)
            total_amount += current_amount
            request.session['gold'] += current_amount
            request.session['activities'] = total_amount
            request.session['location'] = 'cave'
            date_format='%m/%d/%Y %H:%M:%S %Z'
            date = datetime.now(tz=pytz.utc)
            date = date.astimezone(timezone('US/Pacific'))
            myTime = date.strftime(date_format)
            print(myTime)
            str = f"Earned {current_amount} gold from the {location} at {myTime}."
            history.append(str)
            request.session['history'] = history
        if location == 'house':
            current_amount = round(random.random() * 2 + 3)
            total_amount += current_amount
            request.session['gold'] += current_amount
            request.session['activities'] = total_amount
            request.session['location'] = 'house'
            date_format='%m/%d/%Y %H:%M:%S %Z'
            date = datetime.now(tz=pytz.utc)
            date = date.astimezone(timezone('US/Pacific'))
            myTime = date.strftime(date_format)
            print(myTime)
            str = f"Earned {current_amount} gold from the {location} at {myTime}."
            history.append(str)
            request.session['history'] = history 
        if location == 'casino':
            current_amount = round(random.random() * 0 + 50)
            total_amount += current_amount
            request.session['gold'] += current_amount
            request.session['activities'] = total_amount
            request.session['location'] = 'house'
            date_format='%m/%d/%Y %H:%M:%S %Z'
            date = datetime.now(tz=pytz.utc)
            date = date.astimezone(timezone('US/Pacific'))
            myTime = date.strftime(date_format)
            print(myTime)
            str = f"Earned {current_amount} gold from the {location} at {myTime}."
            history.append(str)
            request.session['history'] = history 
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')

# Create your views here.
