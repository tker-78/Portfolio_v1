from django.shortcuts import render
from django.views import generic, View
from django.http import JsonResponse

from datetime import datetime
import requests
import json


class GmoIndexView(generic.TemplateView):
    template_name = 'gmo_index.html'


class ForexStatus(View):

    api_base_url = 'https://forex-api.coin.z.com'
    end_point = '/public/v1/status'

    timeout = 10

    def get(self, request, *args, **kwargs):
        response = requests.get(self.api_base_url + self.end_point)
        data = response.json()
        parsed_time = datetime.strptime(data['responsetime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        strf_time = datetime.strftime(parsed_time, '%Y-%m-%d %H:%M:%S')
        data['responsetime'] = strf_time
        return JsonResponse(data)


