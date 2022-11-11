from typing import Dict

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import http

from django.conf import settings


class Integration:

    def send_data(self):
        ...

    def read_data(self):
        ...


class UserApiIntegration(Integration):

    def preparing_session(self, session=None):
        #http.client.HTTPConnection.debuglevel = 1
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["HEAD", "GET", "POST", "OPTIONS"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        http_request = requests.Session()
        http_request.mount("https://", adapter)
        http_request.mount("http://", adapter)

        return http_request


    def send_data(self, data: Dict):
        headers = { 'Content-Type': 'application/json' }
        session = self.preparing_session()
        try:
            response = session.post(url="http://192.168.96.3:9000/users/", json=data, headers=headers)
            response.raise_for_status()
            data = response.json()
            data.update({'success': True})
            return data
        except Exception as e:
            return {'success': False, 'message': "Por el momento el servicio no está disponible. Favor de intentar más tarde"}
