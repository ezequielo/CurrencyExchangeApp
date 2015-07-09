from behave import given, when, then

@given("a user")
def step_impl(context):
    """
    This step's aim is to create a user and set its pasword so it can be used in the next steps
    :param context:
    """
    from django.contrib.auth.models import User
    u = User(username='test_user', email='testuser@test.com')
    u.set_password('admin')


@when("I log in with username {username} and password {pwd}")
def step_impl(context, username, pwd):
    """
    This is a step intended for login a user given its username and password
    :param context:
    :param username:
    :param pwd: User's password
    :return:
    """
    br = context.browser
    br.get(context.server_url + '/accounts/login/')

    user = br.find_element_by_id("username")
    pswd = br.find_element_by_id("password")

    user.send_keys(username)
    pswd.send_keys(pwd)
    br.find_element_by_id("submit").click()


@then("I go to the {resource} page")
def step_impl(context, resource):
    """
    This is a generic step for getting a URL given the resource ID. If there is not resource ID,
    it will get the root URL
    :param context:
    """
    br = context.browser
    br.get(context.server_url + resource)
    assert br.current_url.endswith(resource)
