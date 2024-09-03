import unittest
from selenium import webdriver
import pytest
import time

@pytest.mark.parametrize("browsers", [1, 2])
class Test_Table():

        def test_table(self, browsers):

                baseurl = "https://www.google.com/"

                if browsers == 1:
                        chrome_options = webdriver.ChromeOptions()
                        chrome_options.add_argument("--incognito")
                        driver = webdriver.Chrome(options=chrome_options)

                elif browsers == 2:
                        ff_options = webdriver.FirefoxOptions()
                        ff_options.add_argument("--headless")
                        driver = webdriver.Firefox(options=ff_options)

                driver.get(baseurl)
                time.sleep(3)
                assert driver.title == "Google"
                time.sleep(3)
                driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)




