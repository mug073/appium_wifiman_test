# Simple tests using python + appium
These are simple samples of how to use Python to run Appium tests.
Test case setup which launches the WiFiman apk.
and next a test case which takes a specific wifi SSID, and prints it’s signal strength every second for 60 seconds, and prints average signal strength after. If the SSID doesn’t exist in the list assert False.
## How ​​to start:
* Activate environment variable
> ` . wifimanenv / bin / activate `
* run appium server
* run emulator
* make sure that the list of available devices emulator exists necessary
> `adb devices`
* run tests
> `py.test -v wifiman.py`
