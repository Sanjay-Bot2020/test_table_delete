import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.chrome.options import Options

class Test_Table(unittest.TestCase):

    def test_table(self):

#         _textbox_Email_id = "Email"
#         _textbox_Password_id = "Password"
#         _button_Login_xpath = "//button[text()='Log in']"
#
#         _link_MainCustomers_xpath = "//li[@class='nav-item has-treeview']/a[@class='nav-link']/p[contains(text(),'Customers')]"
#         _link_Customers_xpath = "//li[@class='nav-item']/a[@href='/Admin/Customer/List']"
#
#         _banner_Search_xpath = "//div[@class='row search-row']"
#         _textbox_SearchEmail_id = "SearchEmail"
#         _button_Search_id = "search-customers"
#
#
#
#
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#         driver.implicitly_wait(10)
#         driver.get("https:\\admin-demo.nopcommerce.com\\login?ReturnUrl=%2Fadmin%2F")
#         driver.find_element(By.ID, _textbox_Email_id).clear()
#         time.sleep(2)
#         driver.find_element(By.ID, _textbox_Password_id).clear()
#         driver.find_element(By.ID, _textbox_Email_id).send_keys("admin@yourstore.com")
#         time.sleep(5)
#         driver.find_element(By.ID, _textbox_Password_id).send_keys("admin")
#         time.sleep(5)
#         driver.find_element(By.XPATH, _button_Login_xpath).click()
#         time.sleep(10)
#
#         alert1 = driver.switch_to.alert
#         alert1.accept()
#         alert1.accept()
#
#         driver.find_element(By.XPATH, _link_MainCustomers_xpath).click()
#         driver.find_element(By.XPATH, _link_Customers_xpath).click()
#
# #         Search Functionality
#
#         driver.find_element(By.XPATH, _banner_Search_xpath).click()
#         driver.find_element(By.ID, _textbox_Email_id).send_keys("victoria_victoria@nopCommerce.com")
#         driver.find_element(By.ID, _button_Search_id).click()
#         time.sleep(5)

        # baseUrl = "https://www.letskodeit.com/practice"
        # baseUrl = "https://www.goibibo.com/"
        # driver = webdriver.Chrome()
        # driver.implicitly_wait(5)
        # driver.get(baseUrl)
        # driver.maximize_window()
        # time.sleep(6)
        #
        # driver.find_element(By.XPATH, "//span[@class='logSprite icClose']").click()
        # hubliToClick = "//ul[@id='autoSuggest-list']//span[text()='Hubli, India']"
        # flights = "//li[@class='sc-1f95z5i-1 kjgDqV']/a[@href='/flights/']"
        # _from = "//input[@type='text']"
        #
        # # driver.find_element(By.XPATH, flights).click()
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//div[@class='sc-12foipm-22 kGtxGm']/div[@class='sc-12foipm-2 eTBlJr fswFld ']").click()
        # driver.find_element(By.XPATH, _from).send_keys("Hubballi")
        # driver.find_element(By.XPATH, hubliToClick).click()
        # time.sleep(3)
        # driver.close()

        baseUrl = "https://www.google.com/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(baseUrl)
        time.sleep(3)
        print(driver.title)
        assert driver.title == "Google"
        time.sleep(3)
        driver.close()
        # _table_CompleteTable_xpath = "//table[@id='product']"
        # CompleteTable = driver.find_element(By.XPATH, _table_CompleteTable_xpath)
        # _forRows_xpath = "//tbody/tr"
        # no_of_rows = CompleteTable.find_elements(By.XPATH, _forRows_xpath)
        # print(len(no_of_rows))
        #
        # for i in range(2, len(no_of_rows)+1):
        #     courseName_dyn = "//tr[{0}]/td[@class='course-name']"
        #     coursePrice_dyn = "//tr[{0}]/td[@class='price']"
        #     courseName_fmt = courseName_dyn.format(i)
        #     coursePrice_fmt = coursePrice_dyn.format(i)
        #     courseName = driver.find_element(By.XPATH, courseName_fmt)
        #     coursePrice = driver.find_element(By.XPATH, coursePrice_fmt)
        #
        #     print(courseName.text, end=" ")
        #     print (coursePrice.text)



if __name__ == "__main__":
    unittest.main(verbosity=2)




