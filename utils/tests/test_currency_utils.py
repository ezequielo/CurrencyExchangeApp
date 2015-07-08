
from django.test import TestCase
from currencyapp.models import Currency, Rate
from utils.currency_utils import get_rate, evaluate
from utils.math_parser import Parser
from utils.custom_exceptions import MathParseException, RateNotFound
import datetime

class CurrencyUtilTest(TestCase):
    """
    This test class aims to test all the utility functions found in
    'currency_utils' file
    """

    def test_get_rate(self):
        """
        This tests aims to check if the latest rate is retrieved in a get_rate()
        function calling, given two currencies as a input parameters.
        """
        c1 = Currency(name='Euro', code='EUR')
        c2 = Currency(name='Dollar', code='USD')
        c1.save()
        c2.save()
        r1 = Rate(date=datetime.date(2015, 5, 24), value=2, sell_ccy=c1, buy_ccy=c2)
        r2 = Rate(date=datetime.date(2015, 5, 20), value=3, sell_ccy=c1, buy_ccy=c2)
        r1.save()
        r2.save()
        rate = get_rate(c1, c2)
        self.assertGreater(r1.date, r2.date)
        self.assertEqual(rate.date, datetime.date(2015, 5, 24))


    def test_get_rate_fails(self):
        """
        In this scenario, get_rate() function fails to find a rate for the given
        currencies, as a result, a 'RateNotFound' exception is raised
        """
        c1 = Currency(name='Euro', code='EUR')
        c1.save()
        c2 = Currency(name='Dollar', code='USD')
        c2.save()
        try:
            get_rate(c1, c2)
            self.fail("Failed to retrieve Rate for the given currencies")
        except RateNotFound:
            raised = True
        self.assertTrue(raised)


    def test_evaluate(self):
        """
        In this scenario, evaluate() function is intended to successfully retrieve
        the exact results of some math operations passed as input parameters
        """
        expr = ('(2*5) + 5 ')
        result = evaluate(expr)
        self.assertEqual(result, 15)
        expr2 = ('(4*(5-2)) + 5 * 6')
        result2 = evaluate(expr2)
        self.assertEqual(result2, 42)


    def test_evaluate_fails(self):
        """
        This is the alternative scenario of evaluate() function. In this scenario the
        calling to the evaluate will raise a 'MathParseException' exception since
        the expressions given as input parameters are not valid
        """
        expr = ('(2*')
        try:
            evaluate(expr)
        except MathParseException:
            raised = True
        self.assertTrue(raised)
