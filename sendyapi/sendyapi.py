# -*- coding: utf-8 -*-
import requests
from requests import RequestException
from .exceptions import SubscriptionError, UnsubscriptionError, HttpRequestError, SubscriberCountError


class SendyAPI(object):

    def __init__(self, base_url, api_key=''):
        self.api_key = api_key
        self.base_url = base_url

    def subscribe(self, name='', email='', list_id='', **kwargs):
        params = {
            'name': name,
            'email': email,
            'list': list_id
        }
        for key, value in kwargs.items():
            params.update({key: value})
        response = self._post('/subscribe', params)

        if response == '1':
            return 'Subscribed'
        else:
            raise SubscriptionError(response)

    def unsubscribe(self, email='', list_id=''):
        params = {
            'email': email,
            'list': list_id
        }
        response = self._post('/unsubscribe', params)

        if response == '1':
            return 'Unsubscribed'
        else:
            raise UnsubscriptionError(response)

    def subscription_status(self, email='', list_id=''):
        params = {
            'email': email,
            'list_id': list_id,
            'api_key': self.api_key
        }
        response = self._post('/api/subscribers/subscription-status.php', params)

        success = ['Subscribed', 'Unsubscribed', 'Unconfirmed', 'Bounced', 'Soft bounced', 'Complained']

        if response in success:
            return response
        else:
            raise UnsubscriptionError(response)

    def subscriber_count(self, list_id=''):
        params = {
            'list_id': list_id,
            'api_key': self.api_key
        }

        response = self._post('/api/subscribers/active-subscriber-count.php', params)

        try:
            return int(response)
        except ValueError:
            raise SubscriberCountError(response)

    def _post(self, path, params):
        url = self.base_url + path
        params.update({'boolean': 'true'})

        try:
            response = requests.post(url, data=params)
            if response.status_code != 200:
                raise HttpRequestError(response.status_code)
            return response.text

        except RequestException as e:
            raise HttpRequestError(e.message)
