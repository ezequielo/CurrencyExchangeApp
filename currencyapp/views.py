from django.shortcuts import render
from forms import ExchangeForm
from django.forms.util import ErrorList
from utils.currency_utils import get_rate
from currencyapp.models import Log
from utils.custom_exceptions import RateNotFound
from django.views.generic import FormView


class CurrencyExchangeView(FormView):
    """
    CurrencyExchangeView is the main view in this app, its aim is to interact with the
    user through the main template, sending and retrieving info requested by the user
    """

    template_name = 'currencyapp/main.html'
    success_url = '#'
    form_class = ExchangeForm

    def form_valid(self, form):
        """
        This view overrides form_valid() method in order to find a rate for the
        currencies in the form, then buy_amount value is computed and returned
        to the user.

        :param form: Form containing sell_amount, sell_ccy and buy_ccy
        :return:
        """

        cd = form.clean()
        sell_amount = cd['amount']
        sell_ccy = cd['sell_ccy']
        buy_ccy = cd['buy_ccy']
        logged_user = self.request.user
        try:
            rate = get_rate(sell_ccy, buy_ccy)
            buy_amount = sell_amount * rate.value
            log = Log(
                sell_amount=sell_amount,
                sell_ccy=sell_ccy,
                buy_amount=buy_amount,
                buy_ccy=buy_ccy,
                rate=rate,
                user=logged_user)
            log.save()
            return render(self.request, 'currencyapp/main.html', {
                'form': ExchangeForm(),
                'res': buy_amount
            })
        except RateNotFound:
            errors = form._errors.setdefault('sell_ccy', ErrorList())
            errors.append(u'Sorry, there is not rate for the given currencies!')
            return render(self.request, 'currencyapp/main.html', {'form': form})
