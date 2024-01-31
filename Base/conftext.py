import pytest

from Base.ObjectManager import Objects


@pytest.fixture()
def make_my_trip_setup():
    obj = Objects()
    Objects.driver = obj.base.open_browser("chrome")
    Objects.wait = obj.base.open_url("https://www.makemytrip.com/")
    obj.initialise_objects(Objects.driver)


@pytest.fixture()
def amazon_setup():
    try:
        obj = Objects()
        Objects.driver = obj.base.open_browser("chrome")
        Objects.wait = obj.base.open_url("https://www.amazon.in/")
        obj.initialise_objects(Objects.driver, Objects.wait)
    except Exception as e:
        print(e)
    yield
    print("completed")


@pytest.fixture(scope="class", name="amazon_data_setup")
def amazon_data_setup():
    try:
        obj = Objects()
        Objects.driver = obj.base.open_browser("chrome")
        Objects.wait = obj.base.open_url("https://www.amazon.in/")
        obj.initialise_objects(Objects.driver, Objects.wait)
    except Exception as e:
        print(e)
    yield
    print("*********************************execution completed*************************************")
