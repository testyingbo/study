# coding=utf-8
from appium import webdriver

deisred_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '5.1.1',
    'appPackage': 'com.sankuai.meituan.takeoutnew',
    'aapActivity': 'com.sankuai.meituan.takeoutnew.ui.page.boot.WelcomeActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', deisred_caps)