from behave import when, then


@when("I fill the form")
def step_impl(context):
    """
    Specific step for filling the ExchangeForm of currencyapp application.
    :param context:
    """
    br = context.browser
    amount = br.find_element_by_id("id_amount")
    sell_ccy = br.find_element_by_id("id_sell_ccy")
    buy_ccy = br.find_element_by_id("id_buy_ccy")

    amount.send_keys("2000")
    sell_ccy.send_keys("Euro EUR")
    buy_ccy.send_keys("Dollar USD")

    br.find_element_by_id("submit").click()


@then("I see {result} in the result section the results")
def step_impl(context, result):
    """
    Specific step for asserting that the results of an operation are correct
    :param context:
    :param result: Expected result of an exchange operation
    """
    br = context.browser
    res = br.find_element_by_id("id_res")
    assert res.text.endswith(result)


@when("I fill the form with the same sell and buy currencies")
def step_impl(context):
    """
    This is a specific currencyapp step for the particular case where sell and buy currencies are the
    same, so the form will not be processed
    :param context:
    """
    br = context.browser
    amount = br.find_element_by_id("id_amount")
    sell_ccy = br.find_element_by_id("id_sell_ccy")
    buy_ccy = br.find_element_by_id("id_buy_ccy")

    amount.send_keys("2000")
    sell_ccy.send_keys("Euro EUR")
    buy_ccy.send_keys("Euro EUR")

    br.find_element_by_id("submit").click()


@then("I see a warning {warning}")
def step_impl(context, warning):
    """
    This step's aim is to assert an error ocurred during the form validation
    :param context:
    :param warning: Expected warning message
    """
    br = context.browser
    res = br.find_element_by_xpath("//form/table/tbody/tr/td/ul[@class='errorlist']/li")
    assert res.text.endswith(warning)