import allure
from allure_commons.types import AttachmentType
from seleniumpagefactory.Pagefactory import PageFactory


class AmazonHome(PageFactory):
    def __init__(self, driver, wait):
        self.driver = driver
        self.timeout = 60
        self.highlight = True
        self.wait = wait

    locators = {
        "amazon_logo": ("ID", "nav-logo-sprites"),
        "home_menu": ("ID", "nav-hamburger-menu"),
        "home_menu_close": ("XPATH", "//div[@class='nav-sprite hmenu-close-icon']"),
        "best_sellers_button": ("XPATH", "//div[text()='trending']/../following-sibling::li/a[text()='Best Sellers']"),
        "new_releases_button": ("XPATH", "//div[text()='trending']/../following-sibling::li/a[text()='New Releases']"),
        "movers_and_shakers_button": ("XPATH", "//div[text()='trending']/../following-sibling::li/a[text()='Movers and Shakers']"),
        "mobiles_computers_category": ("XPATH", "//div[text()='shop by category']/../following-sibling::li//div[text()='Mobiles, Computers']"),
        "all_mobile_phones_button": ("XPATH", "//div[text()='mobiles, tablets & more']/../following-sibling::li/a[text()='All Mobile Phones']"),
        "all_mobile_accessories_button": ("XPATH", "//div[text()='mobiles, tablets & more']/../following-sibling::li/a[text()='All Mobile Accessories']")
    }

    def goto_amazon_home_page(self):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.amazon_logo)
            self.amazon_logo.click_button()
            with allure.step("Click Amazon logo"):
                pass
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def click_best_sellers_button(self):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.home_menu)
            self.home_menu.click_button()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.best_sellers_button)
            self.best_sellers_button.click_button()
            with allure.step("click best sellers button"):
                pass
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def click_new_releases_button(self):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.home_menu)
            self.home_menu.click_button()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.new_releases_button)
            self.new_releases_button.click_button()
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def click_movers_and_shakers_button(self):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.home_menu)
            self.home_menu.click_button()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.movers_and_shakers_button)
            self.movers_and_shakers_button.click_button()
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def click_all_mobile_phones_button(self):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.home_menu)
            self.home_menu.click_button()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.mobiles_computers_category)
            self.mobiles_computers_category.click_button()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.all_mobile_phones_button)
            self.all_mobile_phones_button.click_button()
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def click_all_mobile_accessories_button(self):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.home_menu)
            self.home_menu.click_button()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.mobiles_computers_category)
            self.mobiles_computers_category.click_button()
            self.driver.execute_script("arguments[0].scrollIntoView();", self.all_mobile_accessories_button)
            self.all_mobile_accessories_button.click_button()
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
