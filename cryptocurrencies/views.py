

from django.shortcuts import render

# Create your views here.


def home(request):
    import requests as req
    import json

    #grapping price
    price_request=req.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH,XRP,BTC&tsyms=USD,EUR")
    price=json.loads(price_request.content)
   

   #grapping  cryptonews
    api_request = req.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)


    return render(request,'index.html',{'api':api,'price':price})


def price(request):
    return render(request,'result.html',{})
   