django-paymill
====================

A Django app for integrating with paymill


Installation
------------

1. python setup.py
2. pip install requirements.txt
3. add snowshoestamp to INSTALLED_APPS
4. add url to sss endpoint
5. register url with paymill as webhook callback

Settings
--------


__Required__


```
PAYMILL_KEY : the oauth key for your app
PAYMILL_SECRET : the oauth secret for your app
```


__Example Implementation__

1. Setup your urls.py to use the view below as the callback reciever or just use the default sss reciever
2. Register the url "https://yourhost.com/sss/webhook/" as the webhook callback at snowshoestamp
3. and that is it, you can now hook up the signal listener and get a signal event whenever a webhook event happens

```
url(r'^sss/', include('dj_paymill.urls', namespace='paymill')),
```

__Or__

You can write a custom view, by extending our View and doing somethign more specific with the data, and hook the view up to a url and register that url with snowshoestamp.

```views.py
from dj_paymill.views import PaymillView


class MyPaymillViewWebhookRecieverView(PaymillView):
    def post(self, request, *args, **kwargs):
        # do something amazing

        return self.render_json_response({
            'detail': 'Paymill Callback recieved',
            'data': kwargs
        })
```


__Please Note__

If you use the SnowshoeStampView then a signal will be issued when recieving callbacks from snowshoestamp, which you can then listen for and do other amazing things.


__Signal Example Implementation__


```signals.py
from django.dispatch import receiver

from snowshoestamp.signals import snowshoestamp_event


@receiver(snowshoestamp_event)
def on_snowshoestamp_callback(sender, stamp_serial, **kwargs):
    # do something amazing with the data in the kwargs dict
    pass
```


__TODO__

1. ~~tests~~
2. ~~more descriptive readme.md~~
3. improve setup.py to install from requirements
4. ~~fix broken python_sdk install cant install from pip lacks setup.py~~
