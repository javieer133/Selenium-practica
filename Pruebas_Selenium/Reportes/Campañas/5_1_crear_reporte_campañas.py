# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 51CrearReporteCampanAs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qservus-ppr.redcalidad.com/newsfeed/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_51_crear_reporte_campan_as(self):
        driver = self.driver
        driver.get(self.base_url + "/newsfeed/")
        driver.find_element_by_css_selector("span.fa.fa-file").click()
        driver.find_element_by_css_selector("p.bajada").click()
        driver.find_element_by_css_selector("a.list-group-item.no-item").click()
        driver.find_element_by_css_selector("p.bajada").click()
        driver.find_element_by_link_text("Reporte de respuestasDescargar respuestas en archivo XLS").click()
        driver.find_element_by_xpath("//ul[@id='list_campaigns']/li[3]/a/p").click()
        driver.find_element_by_xpath("//ul[@id='list_campaigns']/li[4]/a/p").click()
        driver.find_element_by_xpath("//ul[@id='list_campaigns']/li[5]/a/p").click()
    
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
