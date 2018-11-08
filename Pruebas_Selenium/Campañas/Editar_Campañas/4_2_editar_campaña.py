# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 42EditarCampanA(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qservus-ppr.redcalidad.com/newsfeed/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_42_editar_campan_a(self):
        driver = self.driver
        driver.get(self.base_url + "/newsfeed/")
        driver.find_element_by_css_selector("span.fa.fa-bullhorn").click()
        driver.find_element_by_css_selector("h2.title").click()
        driver.find_element_by_id("options").click()
        driver.find_element_by_xpath("//ul[@id='menu1']/li[3]/a/span[2]").click()
        driver.find_element_by_id("id_ask_geolocation").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Selenium_edited")
        driver.find_element_by_id("id_email_subject").clear()
        driver.find_element_by_id("id_email_subject").send_keys("Selenium_Test_automated_edited")
        driver.find_element_by_xpath("//button[@type='submit']").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
