from django.conf.urls import patterns, url
from views import CurrencyExchangeView
from django.views.generic import ListView
from models import Log
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'currencyapp/$', login_required(CurrencyExchangeView.as_view()), name="main_page"),
    url(r'currencyapp/logs/$', login_required(ListView.as_view(
        model=Log,
        template_name='currencyapp/logs.html',
    )), name="logs_page"),
)
