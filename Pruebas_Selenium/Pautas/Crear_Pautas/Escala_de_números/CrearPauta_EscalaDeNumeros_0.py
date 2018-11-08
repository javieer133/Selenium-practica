# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CrearPautaEscalaDeNumeros(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_crear_pauta_escala_de_numeros(self):
        driver = self.driver
        driver.get("https://qservus-qa.redcalidad.com/newsfeed/")
        driver.find_element_by_xpath("//li[@id='surveys']/a/span").click()
        driver.find_element_by_id("template_new").click()
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[3]/div/label/span[3]").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys(u"prueba escala de números")
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[4]/div/label/span[3]").click()
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[4]/div/label/span[3]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //form[@id='survey_template_create']/div[2]/div/ul/li[4]/div/label/span[3] | ]]
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[5]/div/label/span[3]").click()
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[5]/div/label/span[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //form[@id='survey_template_create']/div[2]/div/ul/li[5]/div/label/span[2] | ]]
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[6]/div/label/span[3]").click()
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[6]/div/label/span[3]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //form[@id='survey_template_create']/div[2]/div/ul/li[6]/div/label/span[3] | ]]
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='menu_questions']/ul/li[12]/a/span").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("jbsdfbksdf")
        driver.find_element_by_id("id_su_question_type_id").click()
        driver.find_element_by_id("id_su_question_group_tpl").click()
        driver.find_element_by_id("id_su_question_type_id").click()
        Select(driver.find_element_by_id("id_su_question_type_id")).select_by_visible_text(u"7 números (con radio)")
        driver.find_element_by_id("id_su_question_type_id").click()
        Select(driver.find_element_by_id("id_su_question_type_id")).select_by_visible_text(u"10 números (1 al 10)")
        driver.find_element_by_id("id_su_question_type_id").click()
        Select(driver.find_element_by_id("id_su_question_type_id")).select_by_visible_text(u"10 números (0 al 10)")
        driver.find_element_by_id("id_su_question_type_id").click()
        Select(driver.find_element_by_id("id_su_question_type_id")).select_by_visible_text("NPS (con radio)")
        driver.find_element_by_id("id_su_question_type_id").click()
        Select(driver.find_element_by_id("id_su_question_type_id")).select_by_visible_text("NPS (sin radio)")
        driver.find_element_by_id("id_su_question_type_id").click()
        Select(driver.find_element_by_id("id_su_question_type_id")).select_by_visible_text(u"7 números (sin radio)")
        driver.find_element_by_id("id_su_question_group_tpl").click()
        driver.find_element_by_id("show_hide_options").click()
        driver.find_element_by_id("id_help_text").click()
        driver.find_element_by_id("id_help_text").clear()
        driver.find_element_by_id("id_help_text").send_keys("prueba")
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=id_title | ]]
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys(u"prueba escala de números")
        driver.find_element_by_xpath("//form[@id='add_question_scale']/div[3]/label").click()
        driver.find_element_by_id("id_no_apply_label").click()
        driver.find_element_by_id("id_no_apply_label").clear()
        driver.find_element_by_id("id_no_apply_label").send_keys("NO APLICA")
        driver.find_element_by_id("id_priority").click()
        Select(driver.find_element_by_id("id_priority")).select_by_visible_text("100%")
        driver.find_element_by_id("id_justification_type").click()
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
