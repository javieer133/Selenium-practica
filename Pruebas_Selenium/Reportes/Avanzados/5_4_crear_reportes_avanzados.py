# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 54CrearReportesAvanzados(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qservus-ppr.redcalidad.com/newsfeed/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_54_crear_reportes_avanzados(self):
        driver = self.driver
        driver.get(self.base_url + "/newsfeed/")
        driver.find_element_by_css_selector("span.fa.fa-file").click()
        driver.find_element_by_xpath("//ul[@id='entries']/li[4]/a/p").click()
        driver.find_element_by_css_selector("h2.title").click()
        driver.find_element_by_id("id_template_id").click()
        Select(driver.find_element_by_id("id_template_id")).select_by_visible_text("Selenium")
        driver.find_element_by_css_selector("ul.select2-selection__rendered").click()
        driver.find_element_by_id("filter_report").click()
        driver.find_element_by_id("download_report_203").click()
        driver.find_element_by_xpath("//ul[@id='entries']/li[2]/a/h2").click()
        Select(driver.find_element_by_id("id_template_id")).select_by_visible_text("Selenium")
        driver.find_element_by_css_selector("input.select2-search__field").click()
        driver.find_element_by_xpath("//form[@id='date_form_filter']/div[2]/div/div/span/span/span").click()
        driver.find_element_by_id("filter_report").click()
        driver.find_element_by_xpath("//ul[@id='entries']/li[3]/a/h2").click()
        Select(driver.find_element_by_id("id_template_id")).select_by_visible_text("Selenium")
        driver.find_element_by_css_selector("ul.select2-selection__rendered").click()
        driver.find_element_by_xpath("(//input[@type='search'])[2]").click()
        driver.find_element_by_id("filter_report").click()
    
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
