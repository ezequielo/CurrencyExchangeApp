from django.test import TestCase
from currencyapp.forms import ExchangeForm


class ExchangeFormTest(TestCase):
    """
    TestCase class for testing ExchangeForm form. The testing is focused
    on the clean() and clean_field() methods
    """

    def test_valid_data_case1(self):
        """
        In this scenario, a valid form is created and is_valid() method
        should return true
        """

        form = ExchangeForm({
            'amount': '3+500/2',
            'sell_ccy': 1,
            'buy_ccy': 2,
        })
        self.assertTrue(form.is_valid())

    def test_invalid_data_case1(self):
        """
        In this scenario an invalid amount string is provided. clean_amount()
        method can't evaluate the expression and is_valid() method returns False
        """

        form = ExchangeForm({
            'amount': '3+500*',
            'sell_ccy': 1,
            'buy_ccy': 2,
        })
        self.assertFalse(form.is_valid())

    def test_invalid_data_case2(self):
        """
        This is another fail scenario, where sell_ccy and buy_ccy are the same currency.
        In this case, clean() method checks that they are the same and will return an error.

        :return:
        """

        form = ExchangeForm({
            'amount': '3+500/2',
            'sell_ccy': 1,
            'buy_ccy': 1,
        })
        self.assertFalse(form.is_valid())
