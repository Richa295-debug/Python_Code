import pytest

from base.webdriverfactory import WebDriverFactory

@pytest.fixture(scope="class")
def setup(request):
    wdf = WebDriverFactory("chrome")
    driver =wdf.getwebdriver()

    if request.cls is not None:
        request.cls.driver=driver

    print("application is up and running ")

    yield driver

    driver.quit()

    print("closing the browser")