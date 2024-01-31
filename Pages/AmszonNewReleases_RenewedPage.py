import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory


class Renewed(PageFactory):
    def __init__(self, driver, wait):
        self.driver = driver
        self.timeout = 60
        self.highlight = True
        self.wait = wait

    locators = {
        "renewed_items": ("XPATH", "//h1[contains(text(),'Amazon Renewed')]/../following-sibling::div"),
        "any_department_button": ("XPATH", "//a[text()='Any Department']")
    }

    def print_renewed_items(self):
        try:
            print("New Releases in Amazon Renewed")
            self.driver.execute_script("arguments[0].scrollIntoView();", self.renewed_items)
            elements = self.renewed_items.find_elements(By.XPATH, "//div[@id='gridItemRoot']//a/span/div")
            print(len(elements))
            for element in elements:
                print(element.text)
            print("\n")
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def click_any_department_button(self):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.any_department_button)
            self.any_department_button.click_button()
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
