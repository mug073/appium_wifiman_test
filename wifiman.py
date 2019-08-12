import os
import pytest
import time
import numpy

from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '9'
# WIFI_SSID = 'maumau'
WIFI_SSID = 'AndroidWifi'

#app = "https://download.apkpure.com/b/apk/Y29tLnVibnQudXN1cnZleV8xMDMwMTAwMF83YTcxNTIzOQ?_fn=V2lGaW1hbl92MS4zLjFfYXBrcHVyZS5jb20uYXBr&k=0b155999f8a80e86099bd549156aa4b95d4fce58&as=eab232bb40b9702bf73ab6bc1a30bb065d4d2bd0&_p=Y29tLnVibnQudXN1cnZleQ&c=1%7CTOOLS%7CZGV2PVViaXF1aXRpJTIwTmV0d29ya3MlMkMlMjBJbmMuJnQ9YXBrJnM9MTQ3NjgxNjgmdm49MS4zLjEmdmM9MTAzMDEwMDA"


class TestWebViewAndroid():
    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': PLATFORM_VERSION,
            'deviceName': 'Android Emulator',
            'app': PATH('src/wifiman131.apk')
        }
        driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver

    def test_setup_wifiman(self, driver):

# кейс 1 установка приложения
#TODO убрать явные ожидания
        driver.implicitly_wait(10)
#"I\'m in"
        el = driver.find_element_by_android_uiautomator('new UiSelector().text("I\'m in")')
        el.click()
#ALLOW
        el = driver.find_element_by_android_uiautomator('new UiSelector().text("ALLOW")')
        el.click()
#кейс два

#открыть заданную сеть
#"AndroidWifi"
#TODO Ассерт если сеть не найдена
#TODO убрать явные ожидания. Заменить на увеличенное значение ожидание элемента
        driver.implicitly_wait(10)
        el = driver.find_element_by_android_uiautomator(
            # 'new UiScrollable(new UiSelector().instance(0)).scrollIntoView(new UiSelector().text(WIFI_SSID).instance(0));')
            'new UiSelector().text("AndroidWifi")')
        el.click()

#перейти в нее
#чекать каждую секунду в течении 60 секунд и посчитать среднее
        driver.implicitly_wait(10)

        el = driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId(\"com.ubnt.usurvey:id/vSiteDetailGaugeSignalStrengthValue\")'
        ).get_attribute("text")
        print("First signal dBm = " + el)
#вывести среднее и умереть смертью храбрых
        i = 0
        my_list = []
        for _ in range(60):
            el = driver.find_element_by_android_uiautomator(
                'new UiSelector().resourceId(\"com.ubnt.usurvey:id/vSiteDetailGaugeSignalStrengthValue\")'
            ).get_attribute("text")
            el = int(el)
            my_list.append(el)
            # print(i)
            print("Element " + str(i) + " list= " + str(my_list[i]))
            i += 1
            time.sleep(1)

        print("среднее значение: ", end="")
        print(numpy.mean(my_list))


