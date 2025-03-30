from django.shortcuts import render
from django.views import generic, View
from django.http import JsonResponse

from datetime import datetime, timezone
import requests
import json
import pytz


class GmoIndexView(generic.TemplateView):
    template_name = 'gmo_index.html'


class ForexStatus(View):

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

class Ticker(View):

    api_base_url = 'https://forex-api.coin.z.com'
    end_point = '/public/v1/ticker'

    timeout = 10

    def get(self, request, *args, **kwargs):
        response = requests.get(self.api_base_url + self.end_point, *args, **kwargs)
        data = response.json()
        return JsonResponse(data)


