import os
import pytest

from appium import webdriver

# Returns abs path relative to this file and not cwd
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
        return driver  # provide the fixture value

    def test_setup_wifiman(self, driver):

# кейс 1 установка приложения
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
        driver.implicitly_wait(10)
        el = driver.find_element_by_android_uiautomator(
            # 'new UiScrollable(new UiSelector().instance(0)).scrollIntoView(new UiSelector().text("AndroidWifi").instance(0));')
            'new UiSelector().text("AndroidWifi")')
        el.click()

#перейти в нее
#чекать каждую секунду в течении 60 секунд и посчитать среднее
        # self.driver.implicitly_wait(5000)
        driver.implicitly_wait(10)

        el = driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId(\"com.ubnt.usurvey:id/vSiteDetailGaugeSignalStrengthValue\")'
        ).get_attribute("text")
        print("Signal dBm = " + el)
#вывести среднее и умереть смертью храбрых

