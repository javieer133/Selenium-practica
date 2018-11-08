# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 22EditarPauta(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qservus-ppr.redcalidad.com/newsfeed/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_22_editar_pauta(self):
        driver = self.driver
        driver.get(self.base_url + "/newsfeed/")
        driver.find_element_by_css_selector("span.fa.fa-list").click()
        driver.find_element_by_xpath("//ul[@id='entries']/li[3]/a/h2").click()
        driver.find_element_by_xpath("//div[@id='toolbar']/a").click()
        driver.find_element_by_css_selector("span.padding-drop").click()
        driver.find_element_by_id("survey_title").clear()
        driver.find_element_by_id("survey_title").send_keys("Selenium_edited")
        driver.find_element_by_id("survey_desc").clear()
        driver.find_element_by_id("survey_desc").send_keys("Automated testing machine_edited")
        driver.find_element_by_id("validate_first_page").click()
        driver.find_element_by_css_selector(u"a[title=\"El campo a introducir será un texto en una sola línea.\"] > span.label").click()
        driver.find_element_by_id("new_question_name").clear()
        driver.find_element_by_id("new_question_name").send_keys("edited pauta")
        driver.find_element_by_id("new_question_help").clear()
        driver.find_element_by_id("new_question_help").send_keys("pauta editada")
        Select(driver.find_element_by_id("new_question_priority")).select_by_visible_text("100 %")
        driver.find_element_by_link_text("Guardar pregunta").click()
        driver.find_element_by_xpath("//a[@id='save_link']/span").click()
    
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
