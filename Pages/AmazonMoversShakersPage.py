import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory


class MoversAndShakers(PageFactory):
    def __init__(self, driver, wait):
        self.driver = driver
        self.timeout = 60
        self.highlight = True
        self.wait = wait

    locators = {
        "departments": ("XPATH", "//div[@role='group']"),
        "some_movers_and_shakers": ("XPATH", "//div[@id='zg_left_colleft']")
    }

    m_and_s_some_department = "//div[@id='zg_left_col1']/div[contains(@class,'celwidget pd_rd')]"

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

    def print_some_movers_and_shakers(self):
        try:
            departments = self.some_movers_and_shakers.find_elements(By.XPATH, self.m_and_s_some_department)
            print("No. of Departments =", len(departments))
            print()
            for department in departments:
                self.driver.execute_script("arguments[0].scrollIntoView();", department)
                department_name = department.find_element(By.XPATH, "div//h2[contains(text(),'Movers and Shakers')]").text
                print(department_name)
                items = department.find_elements(By.XPATH, "//h2[contains(text(),'" + department_name + "')]/../../following-sibling::div//li//a/span/div")
                print("No. of Items =", len(items))
                for item in items:
                    # self.driver.execute_script("arguments[0].scrollIntoView();", item)
                    print(item.text)
                print()
            print("\n")
        except Exception as e:
            print(e)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
