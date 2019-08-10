import os
import pytest

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '9'

#app = "https://download.apkpure.com/b/apk/Y29tLnVibnQudXN1cnZleV8xMDMwMTAwMF83YTcxNTIzOQ?_fn=V2lGaW1hbl92MS4zLjFfYXBrcHVyZS5jb20uYXBr&k=0b155999f8a80e86099bd549156aa4b95d4fce58&as=eab232bb40b9702bf73ab6bc1a30bb065d4d2bd0&_p=Y29tLnVibnQudXN1cnZleQ&c=1%7CTOOLS%7CZGV2PVViaXF1aXRpJTIwTmV0d29ya3MlMkMlMjBJbmMuJnQ9YXBrJnM9MTQ3NjgxNjgmdm49MS4zLjEmdmM9MTAzMDEwMDA"


class TestWebViewAndroid():
    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_caps = {
            # 'appPackage': 'com.example.android.contactmanager',
            # 'appActivity': '.ContactManager',
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

    def test_add_contacts(self, driver):
        el = driver.find_element_by_accessibility_id("Add Contact")
        el.click()

        textfields = driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("Appium User")
        textfields[2].send_keys("someone@appium.io")

        assert 'Appium User' == textfields[0].text
        assert 'someone@appium.io' == textfields[2].text

        driver.find_element_by_accessibility_id("Save").click()

        # for some reason "save" breaks things
        alert = driver.switch_to_alert()

        # no way to handle alerts in Android
        driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

        driver.press_keycode(3)