from django.test import TestCase
from django.contrib.auth.models import User

class CurrencyappViewTest(TestCase):
    """
    This TestCase class is responsible for testing CurrencyExchangeView view.
    """

    def setUp(self):
        """
        setUp() method is used to preload some data that will be used in
        some of the tests written bellow
        """

        User.objects.create(username='admin', password='')
        user = User.objects.get(username='admin')
        user.set_password('admin')
        user.save()

    def test_login_required_main(self):
        """
        In this test case we check that when /currencyapp/ url is requested by
        an anonymous user, CurrencyExchangeView redirects to login url
        """

        response = self.client.get('/currencyapp/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/currencyapp/')

    def test_login_required_logs(self):
        """
        This test case is similar to the previous one, but the url in this case is
        the logs url (/currencyapp/logs/)
        """

        response = self.client.get('/currencyapp/logs/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/currencyapp/logs/')

    def test_call_view_loads(self):
        """
        This is a successful test case for a logged user requesting an url which is
        login_required-protected
        """

        self.client.login(username='admin', password='admin')
        response = self.client.get('/currencyapp/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'currencyapp/main.html')

    def test_send_valid_form(self):
        """
        A valid test case to check that CurrencyExchangeView works fine. User is
        logged, form is bound with valid data and a rate for the given currencies
        exists.
        """

        self.client.login(username='admin', password='admin')
        response = self.client.post('/currencyapp/',
                                    {'amount': '200',
                                     'sell_ccy': 1,
                                     'buy_ccy': 2
                                     })
        self.assertEqual(response.status_code, 200)

    def test_send_rate_not_found(self):
        """
        In this test case a valid form is sent but the view is not able to find a rate
        for the given currencies. Therefore, it will return an error to the user
        """

        self.client.login(username='admin', password='admin')
        response = self.client.post('/currencyapp/',
                                    {'amount': '200+4',
                                     'sell_ccy': 1,
                                     'buy_ccy': 4
                                     })
        self.assertFormError(response, 'form', 'sell_ccy', 'Sorry, there is not rate for the given currencies!')
        self.assertEqual(response.status_code, 200)

    '''
    def test_send_invalid_form_case1(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post('/currencyapp/',
                                    {'amount': '',
                                     'sell_ccy': 1,
                                     'buy_ccy': 2
                                     })
        self.assertFormError(response, 'form', 'amount', 'This field is required.')
        self.assertEqual(response.status_code, 200)

    def test_send_invalid_form_case2(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post('/currencyapp/',
                                    {'amount': '200+4',
                                     'sell_ccy': 1,
                                     'buy_ccy': 1
                                     })
        self.assertFormError(response, 'form', 'buy_ccy', 'Sell and buy currencies must be different')
        self.assertEqual(response.status_code, 200)
    '''