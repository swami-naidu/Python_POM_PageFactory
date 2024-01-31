# import time
#
# from Base.ObjectManager import Objects
# from Base.conftext import *
#
#
# def test_login(make_my_trip_setup):
#     # obj = Objects()
#     # Objects.driver = obj.base.open_browser("chrome")
#     # Objects.wait = obj.base.open_url("https://www.makemytrip.com/")
#     # obj.initialise_objects(Objects.driver)
#     # BookMyShow code
#     """Objects.object["home"].click_all_cities()
#     time.sleep(2)
#     Objects.object["home"].select_city("Hyderabad")"""
#     Objects.object["home"].close_promo_popup()
#     Objects.object["home"].enter_mobile_number_and_continue("9491670532")
#     otp = int(input("Enter OTP:"))
#     Objects.object["home"].enter_otp(otp)
#     time.sleep(10)
