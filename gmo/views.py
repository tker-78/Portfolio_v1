from django.shortcuts import render
from django.views import generic, View
from django.http import JsonResponse

from .models import KLine

from datetime import datetime, timezone
import requests
import json
import pytz


class GmoIndexView(generic.TemplateView):
    template_name = 'gmo_index.html'


class ForexStatusAPI(View):

    api_base_url = 'https://forex-api.coin.z.com'
    end_point = '/public/v1/status'

    timeout = 10

    def get(self, request, *args, **kwargs):
        response = requests.get(self.api_base_url + self.end_point)
        data = response.json()
        parsed_time = datetime.strptime(data['responsetime'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
        local_timezone = pytz.timezone('Asia/Tokyo')
        local_time = parsed_time.astimezone(local_timezone)
        strf_time = datetime.strftime(local_time, '%Y-%m-%d %H:%M:%S')
        data['responsetime'] = strf_time
        return JsonResponse(data)

class TickerAPI(View):

    api_base_url = 'https://forex-api.coin.z.com'
    end_point = '/public/v1/ticker'

    timeout = 10

    def get(self, request, *args, **kwargs):
        response = requests.get(self.api_base_url + self.end_point, *args, **kwargs)
        data = response.json()
        return JsonResponse(data)

class KLinesAPI(View):

    api_base_url = 'https://forex-api.coin.z.com'
    end_point = '/public/v1/klines'

    def get(self, request, *args, **kwargs):

        # クエリパラメータを取得
        symbol = request.GET.get('symbol', 'USD_JPY')
        print(symbol)
        priceType = request.GET.get('priceType', 'ASK')
        interval = request.GET.get('interval', '1hour')
        date_today = datetime.now().replace(tzinfo=timezone.utc).astimezone(pytz.timezone('Asia/Tokyo'))
        date_today = datetime.strftime(date_today, "%Y-%m-%d")
        date = request.GET.get('date', date_today)

        params = {
            'symbol': symbol,
            'priceType': priceType,
            'interval': interval,
            'date': date
        }

        response = requests.get(self.api_base_url + self.end_point, params=params)

        data = response.json()
        klines = data['data']

        for kline in klines:
            self.generate_kline(kline)



        return JsonResponse(data)


    def generate_kline(self, kline_data: dict):

        # format of kline_data: {'openTime': '1743109200000', 'open': '151.096', 'high': '151.109', 'low': '151.067', 'close': '151.095'}
        timestamp = kline_data['openTime']
        time = datetime.fromtimestamp(int(timestamp) / 1000)


        kline = KLine(
            time=time,
            open=float(kline_data['open']),
            high=float(kline_data['high']),
            low=float(kline_data['low']),
            close=float(kline_data['close']),
        )

        kline.save()

        return








