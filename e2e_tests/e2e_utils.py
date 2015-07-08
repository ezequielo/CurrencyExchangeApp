__author__ = 'ebury'
import os


def get_driver_path(driver='chromedriverold'):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'drivers', driver)