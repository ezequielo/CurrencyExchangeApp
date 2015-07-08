from django.forms.util import ErrorList
from utils.currency_utils import evaluate
from utils.custom_exceptions import MathParseException

__author__ = 'ebury'

from django import forms
from models import Currency

class ExchangeForm(forms.Form):
    """
    This form is responsible for retrieving the currency exchange info
    such as sell currency, amount and the desired buy currency
    """
    amount = forms.CharField()
    sell_ccy = forms.ModelChoiceField(queryset=Currency.objects.all())
    buy_ccy = forms.ModelChoiceField(queryset=Currency.objects.all())

    def clean(self):
        """
        Override of clean method in order to evaluate that sell and buy currencies set
        by the user are different
        :return: cleaned fields
        """
        if self.data['sell_ccy'] == self.data['buy_ccy'] and self.data['sell_ccy'] != '':
            errors = self._errors.setdefault('buy_ccy', ErrorList())
            errors.append(u'Sell and buy currencies must be different')
        else:
            return super(ExchangeForm, self).clean()

    def clean_amount(self):
        """
        clean_amount() method validates the amount field using evaluate() function
        defined in the utils package
        :return: cleaned amount field
        """
        amount = self.cleaned_data['amount']
        try:
            amount = float(evaluate(amount))

        except MathParseException:
            errors = self._errors.setdefault('amount', ErrorList())
            errors.append(u'Please, write a valid expression or a number')

        return amount
