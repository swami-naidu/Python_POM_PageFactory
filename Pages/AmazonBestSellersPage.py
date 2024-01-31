import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory


class AmazonBestSellers(PageFactory):
    def __init__(self, driver, wait):
        self.driver = driver
        self.timeout = 60
        self.highlight = True
        self.wait = wait

    locators = {
        "departments": ("XPATH", "//div[@role='tree']"),
        "bags_wallets_luggage": ("XPATH", "//h2[contains(text(), 'Bags, Wallets and Luggage')]/../../following-sibling::div//ol"),
        "video_games": ("XPATH", "//h2[contains(text(), 'Video Games')]/../../following-sibling::div//ol"),
        "music": ("XPATH", "//h2[contains(text(), 'Music')]/../../following-sibling::div//ol"),
        "renewed": ("XPATH", "//h2[contains(text(), 'Amazon Renewed')]/../../following-sibling::div//ol"),
        "office_products": ("XPATH", "//h2[contains(text(), 'Office Products')]/../../following-sibling::div//ol"),
        "Industrial_and_scientific": ("XPATH", "//h2[contains(text(), 'Industrial & Scientific')]/../../following-sibling::div//ol"),
    }

    def print_departments(self):
        try:
            print("Departments in BestSellers:")
            self.driver.execute_script("arguments[0].scrollIntoView();", self.departments)
            elements = self.departments.find_elements(By.XPATH, "div/div/a")
            print(len(elements))
            for element in elements:
                print(element.text)
            print("\n")
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def print_best_sellers_in_bags_wallets_luggage(self):
        print("BestSellers in Bags, Wallets and Luggage:")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.bags_wallets_luggage)
        elements = self.bags_wallets_luggage.find_elements(By.XPATH, "li/div/div/a/span/div")
        print(len(elements))
        for element in elements:
            print(element.text)
        print("\n")

    def print_best_sellers_in_video_games(self):
        print("BestSellers in Video Games:")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.video_games)
        elements = self.video_games.find_elements(By.XPATH, "li/div/div/a/span/div")
        print(len(elements))
        for element in elements:
            print(element.text)
        print("\n")

    def print_best_sellers_in_music(self):
        print("BestSellers in Music:")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.music)
        elements = self.music.find_elements(By.XPATH, "li/div/div/a/span/div")
        print(len(elements))
        for element in elements:
            print(element.text)
        print("\n")

    def print_best_sellers_in_amazon_renewed(self):
        print("BestSellers in Amazon Renewed:")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.renewed)
        elements = self.renewed.find_elements(By.XPATH, "li/div/div/a/span/div")
        print(len(elements))
        for element in elements:
            print(element.text)
        print("\n")

    def print_best_sellers_in_office_products(self):
        print("BestSellers in Office Products:")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.office_products)
        elements = self.office_products.find_elements(By.XPATH, "li/div/div/a/span/div")
        print(len(elements))
        for element in elements:
            print(element.text)
        print("\n")

    def print_best_sellers_in_industrial_and_scientific(self):
        print("BestSellers in Industrial & Scientific:")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.Industrial_and_scientific)
        elements = self.Industrial_and_scientific.find_elements(By.XPATH, "li/div/div/a/span/div")
        print(len(elements))
        for element in elements:
            print(element.text)
        print("\n")
