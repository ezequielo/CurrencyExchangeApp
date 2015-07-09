__author__ = 'ebury'

from currencyapp.models import Rate
from math_parser import Parser
from utils.custom_exceptions import MathParseException, RateNotFound


def get_rate(sell_ccy, buy_ccy):
    """
    Given two pair of currencies, get_rate() function is able to find
    the latest rate for both values.

    :param currency_in: Sell currency
    :param currency_out: Purchase currency
    :return: Latest rate for both currencies
    """

    try:
        rate = Rate.objects.filter(sell_ccy=sell_ccy, buy_ccy=buy_ccy).order_by('-date')[0]
    except IndexError as e:
        raise RateNotFound("Unable to find a rate for the given currencies!")
    return rate


def evaluate(expression):
    """
    This function is able to create a Parser object and retrieve the value
    given a math expression contained in a string

    :param expression: String object containing a math expression
    :return: Result of the math expression
    """

    p = Parser(expression)
    try:
        value = p.get_value()
    except MathParseException as e:
        raise MathParseException(e.message)
    return value


