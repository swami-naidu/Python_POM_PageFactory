# import time
#
# from selenium.webdriver.common.by import By
# from seleniumpagefactory.Pagefactory import PageFactory
#
#
# class Home(PageFactory):
#     def __init__(self, driver):
#         self.driver = driver
#         self.timeout = 60
#         self.highlight = True
#
#     # BookMyShow Home page
#     """locators = {
#         "view_all_cities": ("XPATH", "//span[text()='View All Cities']"),
#         "city": ("XPATH", "")
#     }
#
#     def click_all_cities(self):
#         self.view_all_cities.click_button()
#
#     def select_city(self, city_name):
#         xpath = "(//li//*[contains(text(),'" + city_name + "')])[1]"
#         Home.locators["city"] = ("XPATH", xpath)
#         self.city.click_button()"""
#
#     locators = {
#         "notification_frame": ("XPATH", "//iframe[contains(@name, 'notification-frame')]"),
#         "promo_popup_close_button": ("XPATH", "//a[contains(@id, 'notification-close-div')]"),
#         "make_my_trip_logo": ("XPATH", "//img[@alt='Make My Trip']"),
#         "mobile_number_text_box": ("ID", "username"),
#         "login_continue_button": ("XPATH", "//button[@data-cy='continueBtn']"),
#         "login_with_password_link": ("XPATH", "//a[text()='or Login via OTP']"),
#         "password_text_box": ("ID", "password"),
#         "login_button": ("XPATH", "//button[@data-cy='login']"),
#         "otp_text_box": ("ID", "otp"),
#     }
#
#     def close_promo_popup(self):
#         time.sleep(2)
#         self.driver.switch_to.frame(self.notification_frame)
#         time.sleep(2)
#         self.promo_popup_close_button.click_button()
#         time.sleep(2)
#         self.driver.switch_to.default_content()
#
#     def enter_mobile_number_and_continue(self, number):
#         self.mobile_number_text_box.clear_text()
#         self.mobile_number_text_box.set_text(str(number))
#         time.sleep(2)
#         self.login_continue_button.click_button()
#         time.sleep(2)
#
#     def enter_otp(self, otp):
#         self.otp_text_box.clear_text()
#         self.otp_text_box.set_text(otp)
#         time.sleep(2)
#         self.login_button.click_button()
#         time.sleep(2)
