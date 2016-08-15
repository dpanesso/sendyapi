# SendyAPI

Python wrapper to use with Sendy's API.

Sendy API documentation: https://sendy.co/api

## Usage

```Python
  sendyapi = SendyAPI(base_url='http://YOUR_SENDY_URL/', api_key='YOUR_API_KEY')
```

### Subscription

```Python
try:
  result = sendyapi.subscribe(name='David', email='david@example.com', list_id='YOUR_LIST_ID', custom_field_1='custom_value_1')
except SubscriptionError as e:
  print e.message
```
