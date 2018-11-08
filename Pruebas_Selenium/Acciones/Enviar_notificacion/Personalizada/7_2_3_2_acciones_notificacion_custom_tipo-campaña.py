# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 7232AccionesNotificacionCustomTipoCampanA(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qservus-ppr.redcalidad.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_7232_acciones_notificacion_custom_tipo_campan_a(self):
        driver = self.driver
        driver.get(self.base_url + "/newsfeed/")
        driver.find_element_by_css_selector("span.fa.fa-actions").click()
        driver.find_element_by_xpath("//div[@id='content']/div[3]/div/ul/li[2]/a/p").click()
        driver.find_element_by_link_text("Alerta personalizadaEncuestas configuradas: 1").click()
        driver.find_element_by_xpath("//div[@id='content']/div[2]/a").click()
        Select(driver.find_element_by_id("id_survey_type")).select_by_visible_text(u"Campaña")
        Select(driver.find_element_by_id("id_su_survey")).select_by_visible_text("Selenium_edited (1)")
        driver.find_element_by_id("id_subject").clear()
        driver.find_element_by_id("id_subject").send_keys("Selenium Custom")
        driver.find_element_by_id("id_add_extra_data").click()
        driver.find_element_by_id("id_send_extra_data").click()
        driver.find_element_by_id("id_receivers_0").click()
        driver.find_element_by_id("id_receivers_cc_1").click()
        driver.find_element_by_id("create_event_custom").click()
    
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
