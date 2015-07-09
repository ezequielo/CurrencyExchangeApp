from behave import given, when, then

@given("a user")
def step_impl(context):
    from django.contrib.auth.models import User
    u = User(username='test_user', email='testuser@test.com')
    u.set_password('admin')


@when("I log in")
def step_impl(context):
    br = context.browser
    br.get(context.server_url + '/accounts/login/')

    user = br.find_element_by_id("username")
    pswd = br.find_element_by_id("password")

    user.send_keys("admin")
    pswd.send_keys("admin")
    br.find_element_by_id("submit").click()


@then("I go to the main page")
def step_impl(context):
    br = context.browser
    br.get(context.server_url + '/currencyapp/')
    assert br.current_url.endswith('/currencyapp/')


@when("I fill the form")
def step_impl(context):
    br = context.browser
    amount = br.find_element_by_id("id_amount")
    sell_ccy = br.find_element_by_id("id_sell_ccy")
    buy_ccy = br.find_element_by_id("id_buy_ccy")

    amount.send_keys("2000")
    sell_ccy.send_keys("Euro EUR")
    buy_ccy.send_keys("Dollar USD")

    br.find_element_by_id("submit").click()

@then("I see the results")
def step_impl(context):
    br = context.browser
    res = br.find_element_by_id("id_res")
    assert res.text.endswith('2300.000')


@when("I log in with username {username} and password {pwd}")
def step_impl(context, username, pwd):
    br = context.browser
    br.get(context.server_url + '/accounts/login/')

    user = br.find_element_by_id("username")
    pswd = br.find_element_by_id("password")

    user.send_keys(username)
    pswd.send_keys(pwd)
    br.find_element_by_id("submit").click()


@when("I fill the form with the same sell and buy currencies")
def step_impl(context):
    br = context.browser
    amount = br.find_element_by_id("id_amount")
    sell_ccy = br.find_element_by_id("id_sell_ccy")
    buy_ccy = br.find_element_by_id("id_buy_ccy")

    amount.send_keys("2000")
    sell_ccy.send_keys("Euro EUR")
    buy_ccy.send_keys("Euro EUR")

    br.find_element_by_id("submit").click()


@then("I see a warning")
def step_impl(context):
    br = context.browser
    res = br.find_element_by_xpath("//form/table/tbody/tr/td/ul[@class='errorlist']/li")
    assert res.text.endswith('Sell and buy currencies must be different')