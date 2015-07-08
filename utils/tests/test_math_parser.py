
from django.test import TestCase
from currencyapp.models import Currency, Rate
from utils.currency_utils import get_rate, evaluate
from utils.math_parser import Parser
from utils.custom_exceptions import MathParseException, RateNotFound
import datetime


class MathParserTest(TestCase):
    """
    Test class for testing MathParser methods
    """

    def get_value(self):
        """
        Unit test responsible of checking the get_value() method
        implemented in Parse class
        """
        expr = '(2*5) + 5 '
        p = Parser(expr)
        result = p.get_value()
        self.assertEqual(result, 15)

        expr2 = '200 * (5+6) /4 + 3'
        p2 = Parser(expr2)
        result2 = p2.get_value()
        self.assertEqual(result2, 553)


    def test_parse_number(self):
        """
        This test aims to check if the parse_number() function defined inside
        Parse class is able to correctly detect numbers
        :return:
        """
        expr = ' 5'
        p = Parser(expr)
        self.assertEqual(p.parse_number(), 5)

        expr = '345.5'
        p2 = Parser(expr)
        self.assertEqual(p2.parse_number(), 345.5)


    def test_parse_number_fails_1(self):
        """
        In this test parse_number() method is checked. It should return an
        exception since the string passed as attribute doesn't represent
        a number
        """
        expr = '('
        p = Parser(expr)

        try:
            p.parse_number()
        except MathParseException:
            raised = True
        self.assertTrue(raised)

    def test_parse_number_fails_2(self):
        """
        In this test parse_number() method is checked. It should return an
        exception since there are more than one dot in the given string
        """
        expr = '345..5'
        p = Parser(expr)

        try:
            p.parse_number()
        except MathParseException:
            raised = True
        self.assertTrue(raised)


    def test_parse_multiplication(self):
        """
        parse_multiplication() method is checked in this test in order to
        assure it works properly, given a multiplication operation contained
        in a string as a input param
        """
        expr = '1/(5+7)'
        p = Parser(expr)
        result = p.parse_multiplication()
        self.assertEqual(result, 1.0/12.0)


    def test_parse_multiplication_fails(self):
        """
        In this test division by zero is checked since it's not possible to
        make this operation, parse_multiplication() method should raise a
        'MathParseException' so that it can be handled in the rest of the code
        """
        expr = '5/0'
        p = Parser(expr)

        try:
            p.parse_multiplication()
        except MathParseException:
            raised = True
        self.assertTrue(raised)
