import os

from pyvirtualdisplay import Display
from selenium import webdriver
from e2e_tests.e2e_utils import get_driver_path

os.environ['DJANGO_SETTINGS_MODULE'] = 'myapp.settings'


def before_all(context):

    context.display = Display(visible=1, size=(1920, 1080))
    context.display.start()
    chromedriver = get_driver_path()
    os.environ["webdriver.chrome.driver"] = chromedriver
    context.browser = webdriver.Chrome(chromedriver)
    context.browser.implicitly_wait(10)
    context.browser.set_window_size(1920, 1080)
    context.browser.set_window_position(0, 0)
    context.browser.implicitly_wait(10)
    context.server_url = 'http://127.0.0.1:8000'


def after_all(context):

    context.display.stop()
    context.browser.quit()
