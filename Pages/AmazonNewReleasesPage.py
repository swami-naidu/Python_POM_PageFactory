import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory


class AmazonNewReleases(PageFactory):
    def __init__(self, driver, wait):
        self.driver = driver
        self.timeout = 60
        self.highlight = True
        self.wait = wait

    locators = {
        "departments": ("XPATH", "//div[@role='group']"),
        "department_amazon_renewed": ("XPATH", "//a[text()='Amazon Renewed']"),
        "department_baby_products": ("XPATH", "//a[text()='Baby Products']")
    }

    def print_departments(self):
        try:
            print("Departments in NewReleases:")
            self.driver.execute_script("arguments[0].scrollIntoView();", self.departments)
            elements = self.departments.find_elements(By.XPATH, "div/a")
            print(len(elements))
            for element in elements:
                print(element.text)
            print('\n')
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def click_department_amazon_renewed(self):
        try:
            self.department_amazon_renewed.click_button()
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def click_department_baby_products(self):
        try:
            self.department_baby_products.click_button()
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

