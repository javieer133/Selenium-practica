# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class PreguntasTextoCompleto(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qservus-qa.redcalidad.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_preguntas_texto_completo(self):
        driver = self.driver
        driver.get(self.base_url + "/login/sign_in/")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("daniel.hebel@sansano.usm.cl")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("practica_qservus")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_xpath("//li[@id='surveys']/a/span").click()
        driver.find_element_by_id("template_new").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("Preguntas de texto Complea")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Texto").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("100%, simple, numero, min 5, max10")
        driver.find_element_by_id("id_help_text").click()
        driver.find_element_by_id("id_help_text").clear()
        driver.find_element_by_id("id_help_text").send_keys("esta es la primera pregunta")
        driver.find_element_by_id("id_priority").click()
        Select(driver.find_element_by_id("id_priority")).select_by_visible_text("100%")
        driver.find_element_by_xpath("//option[@value='1']").click()
        driver.find_element_by_id("id_validation_type").click()
        Select(driver.find_element_by_id("id_validation_type")).select_by_visible_text(u"Número")
        driver.find_element_by_xpath("(//option[@value='1'])[3]").click()
        driver.find_element_by_id("id_min_length").click()
        driver.find_element_by_id("id_min_length").clear()
        driver.find_element_by_id("id_min_length").send_keys("5")
        driver.find_element_by_id("id_max_length").click()
        driver.find_element_by_id("id_max_length").click()
        driver.find_element_by_id("id_max_length").clear()
        driver.find_element_by_id("id_max_length").send_keys("10")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Texto").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("100%, multilinea, min5, max5")
        driver.find_element_by_id("id_help_text").click()
        driver.find_element_by_id("id_help_text").clear()
        driver.find_element_by_id("id_help_text").send_keys("esta es la segunda pregunta")
        driver.find_element_by_id("id_priority").click()
        Select(driver.find_element_by_id("id_priority")).select_by_visible_text("100%")
        driver.find_element_by_xpath("//option[@value='1']").click()
        driver.find_element_by_id("id_su_question_type_id").click()
        Select(driver.find_element_by_id("id_su_question_type_id")).select_by_visible_text("Texto multilinea")
        driver.find_element_by_xpath("(//option[@value='2'])[2]").click()
        driver.find_element_by_id("id_min_length").click()
        driver.find_element_by_id("id_min_length").clear()
        driver.find_element_by_id("id_min_length").send_keys("5")
        driver.find_element_by_id("id_max_length").click()
        driver.find_element_by_id("id_max_length").clear()
        driver.find_element_by_id("id_max_length").send_keys("5")
        driver.find_element_by_xpath("//div[@id='modal']/div/div").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Texto").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("100%, simple, correo electronico")
        driver.find_element_by_id("id_priority").click()
        Select(driver.find_element_by_id("id_priority")).select_by_visible_text("100%")
        driver.find_element_by_xpath("//option[@value='1']").click()
        driver.find_element_by_id("id_validation_type").click()
        Select(driver.find_element_by_id("id_validation_type")).select_by_visible_text(u"Correo electrónico")
        driver.find_element_by_xpath("//option[@value='4']").click()
        driver.find_element_by_id("id_help_text").click()
        driver.find_element_by_id("id_help_text").clear()
        driver.find_element_by_id("id_help_text").send_keys("Esta es la tercera pregunta")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Texto").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("nada, multilinea")
        driver.find_element_by_id("id_help_text").click()
        driver.find_element_by_id("id_help_text").clear()
        driver.find_element_by_id("id_help_text").send_keys("esta es la cuarta pregunta")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div[4]/ul/li[2]/a").click()
        driver.find_element_by_id("id_su_question_type_id").click()
        Select(driver.find_element_by_id("id_su_question_type_id")).select_by_visible_text("Texto multilinea")
        driver.find_element_by_xpath("(//option[@value='2'])[2]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//ul[@id='pautas_tab']/li[2]/a").click()
    
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
