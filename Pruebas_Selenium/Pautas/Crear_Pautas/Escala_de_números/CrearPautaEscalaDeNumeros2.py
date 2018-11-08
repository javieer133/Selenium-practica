# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CrearPautaEscalaDeNumeros2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_crear_pauta_escala_de_numeros2(self):
        driver = self.driver
        driver.get("https://qservus-qa.redcalidad.com/newsfeed/")
        driver.find_element_by_xpath("//li[@id='surveys']/a/span").click()
        driver.find_element_by_id("template_new").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("CrearPauta_EscalaDeNumeros_2")
        driver.find_element_by_id("id_subtitle").click()
        driver.find_element_by_id("id_subtitle").clear()
        driver.find_element_by_id("id_subtitle").send_keys("CrearPauta_EscalaDeNumeros_1")
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[4]/div/label/span[3]").click()
        driver.find_element_by_xpath("//html").click()
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[4]/div/label/span[3]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='menu_questions']/ul/li[12]/a/span").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("CrearPauta_EscalaDeNumeros_2")
        driver.find_element_by_id("id_su_question_type_id").click()
        Select(driver.find_element_by_id("id_su_question_type_id")).select_by_visible_text(u"10 números (1 al 10)")
        driver.find_element_by_id("id_su_question_group_tpl").click()
        driver.find_element_by_xpath("//div[@id='show_hide_options']/span").click()
        driver.find_element_by_id("id_help_text").click()
        driver.find_element_by_id("id_help_text").clear()
        driver.find_element_by_id("id_help_text").send_keys("CrearPauta_EscalaDeNumeros_2")
        driver.find_element_by_id("id_priority").click()
        Select(driver.find_element_by_id("id_priority")).select_by_visible_text("30%")
        driver.find_element_by_id("id_justification_type").click()
        Select(driver.find_element_by_id("id_justification_type")).select_by_visible_text("Justificar en todas las notas")
        driver.find_element_by_xpath("//form[@id='add_question_scale']/div[4]/label").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//ul[@id='pautas_tab']/li[2]/a/span").click()
    
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
