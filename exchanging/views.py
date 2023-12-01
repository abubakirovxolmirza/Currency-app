from django.shortcuts import render
import requests
from . import models
from .models import Currency


def index(request):
    if request.method == "POST":
        try:
            amount = float(request.POST.get('amount'))
            from_money = request.POST.get("currency_from")
            to_money = request.POST.get("currency_to")
            date = request.POST.get("date")
        except ValueError:
            return render(request, 'exchanging/index.html')

        url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{from_money.lower()}/{to_money.lower()}.json'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            converted_amount = amount * data[to_money.lower()]
            Currency.objects.create(
                amount=amount,
                from_money=from_money,
                converted_amount=converted_amount,
                to_money=to_money,
            )
            return render(request, 'exchanging/index.html', {'result': converted_amount, 'currency_to': to_money})
        else:
            return render(request, 'exchanging/index.html')
    return render(request, 'exchanging/index.html')



def history(request):
    return render(request, 'exchanging/history.html', {'currencies': models.Currency.objects.all()})