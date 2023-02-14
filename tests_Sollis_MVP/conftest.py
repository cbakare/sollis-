
import pytest
from selenium import webdriver
import urllib3


@pytest.fixture(scope="class")
def setup(request):
    urllib3.disable_warnings()
    caps = {
        'username': 'anithap',
        'accessKey': '749be6bd-b53e-46a8-9dd4-5880090beecf',
        'deviceName': 'iPhone.*',
        'platformName': 'iOS',
        'browserName': 'Safari',
        'deviceOrientation': 'portrait',
        "autoAcceptAlerts": 'true'

    }
    url="https://anithap:749be6bd-b53e-46a8-9dd4-5880090beecf@ondemand.us-west-1.saucelabs.com:443/wd/hub"

    driver= webdriver.Remote(
        command_executor=url,
        desired_capabilities=caps,
        keep_alive=True
       )
    driver.get("https://memberportal4testing.z13.web.core.windows.net")
    request.cls.driver = driver
    yield
    driver.quit()















from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# @pytest.fixture(scope="class")
# def setup(request):
#     global driver
#     desired_cap = {
#         'browserName': 'iphone',
#         'device': 'iPhone 11',
#         'realMobile': 'true',
#         'os_version': '13.1',
#         'name': 'BStack-[Python] Sample Test',  # test name
#         'build': 'BStack Build Number 1'  # CI/CD job or build name
#     }
#     driver = webdriver.Remote(
#         command_executor='https://sollistester_wH7NuV:ZT6UACZDanCpya71HB7t@hub-cloud.browserstack.com/wd/hub',
#         desired_capabilities=desired_cap)
#     driver.get("https://memberportal4testing.z13.web.core.windows.net/")
#     request.cls.driver=driver
#     yield
#     driver.quit()












# @pytest.fixture
# def LoginpageDataloader():
#     return  ["prameela.b@lancesoft.com","Password1234$"]
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)

@pytest.fixture(params=[("prameela.b@lancesoft.com","Password1234$")])
def LoginpageDataloader(request):
    return request.param

