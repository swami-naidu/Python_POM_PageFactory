import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory


class AllMobilePhones(PageFactory):
    def __init__(self, driver, wait):
        self.driver = driver
        self.timeout = 60
        self.highlight = True
        self.wait = wait

    locators = {
        "body": ("XPATH", "//body"),
        "all_brands": ("XPATH", "//span[text()='Brands']/../following-sibling::ul"),
        "brand_results": ("XPATH", "//span[@data-component-type='s-search-results']")
    }

    images_xpath = "//img[contains(@alt,' ')]"
    validate_brand_name = "li//span[@dir='auto']"

    def print_data(self):
        try:
            print("All mobiles")
            images = self.body.find_elements(By.XPATH, self.images_xpath)
            print("No. of Items =", len(images))
            for image in images:
                print(image.get_attribute("alt"))
            print("\n")
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def print_brand_data(self):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.all_brands)
            brands = self.all_brands.find_elements(By.XPATH, self.validate_brand_name)
            print("\nNo. of brands =", len(brands), "\n\nEnter one of the following brands")
            for brand in brands:
                print(brand.text)
            # brand_name = input("Enter required brand:")
            brand_name = "abc"
            print("\n", brand_name, "Mobiles")
            i = 0
            for brand in brands:
                i = i + 1
                if brand.text == brand_name:
                    # brand.click_button()
                    self.all_brands.find_element(By.XPATH, "li[" + str(i) + "]//div//i").click()
                    break
            else:
                print("Enter a valid brand")
                return
            mobiles = self.brand_results.find_elements(By.XPATH, "//h2//span")
            print("No. of Items =", len(mobiles))
            for mobile in mobiles:
                print(mobile.text)
            print("\n")
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
