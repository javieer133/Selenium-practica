# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 7112AccionesObteneropinionFelicitacionesTipoCampanA(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qservus-ppr.redcalidad.com/newsfeed/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_7112_acciones_obteneropinion_felicitaciones_tipo_campan_a(self):
        driver = self.driver
        driver.get(self.base_url + "/newsfeed/")
        driver.find_element_by_css_selector("span.fa.fa-actions").click()
        driver.find_element_by_link_text(u"Obtener opiniónAcciones para obtener un feedback extra por parte de quienes contestan las encuestas").click()
        driver.find_element_by_css_selector("p.bajada").click()
        driver.find_element_by_xpath("//div[@id='content']/div[2]/a").click()
        Select(driver.find_element_by_id("id_survey_type")).select_by_visible_text(u"Campaña")
        Select(driver.find_element_by_id("id_su_survey")).select_by_visible_text("Selenium_edited (1)")
        Select(driver.find_element_by_id("id_su_question")).select_by_visible_text(u"Cuán satisfecho está usted con el precio del producto?")
        driver.find_element_by_id("id_receivers_0").click()
        driver.find_element_by_id("id_receivers_cc_1").click()
        driver.find_element_by_id("create_event").click()
    
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
