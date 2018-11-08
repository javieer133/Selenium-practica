# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CrearPautaMatriz(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_crear_pauta_matriz(self):
        driver = self.driver
        driver.get("https://qservus-qa.redcalidad.com/newsfeed/")
        driver.find_element_by_xpath("//li[@id='surveys']/a/span").click()
        driver.find_element_by_id("template_new").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("crear pauta matriz")
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[3]/div/label/span[3]").click()
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[3]/div/label/span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //form[@id='survey_template_create']/div[2]/div/ul/li[3]/div/label/span | ]]
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[3]/div/label/span[3]").click()
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[4]/div/label/span[3]").click()
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[4]/div/label/span[3]").click()
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[5]/div/label/span[3]").click()
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[5]/div/label/span[3]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //form[@id='survey_template_create']/div[2]/div/ul/li[5]/div/label/span[3] | ]]
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[6]/div/label/span[3]").click()
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div[2]/div/ul/li[6]/div/label/span[3]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //form[@id='survey_template_create']/div[2]/div/ul/li[6]/div/label/span[3] | ]]
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='menu_questions']/ul/li[14]/a/span").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("prueba matriz")
        driver.find_element_by_id("id_matrix_type").click()
        Select(driver.find_element_by_id("id_matrix_type")).select_by_visible_text(u"Matriz de escala de 7 números")
        driver.find_element_by_id("id_matrix_type").click()
        Select(driver.find_element_by_id("id_matrix_type")).select_by_visible_text("Matriz de escala de 0 al 10")
        driver.find_element_by_id("id_matrix_type").click()
        Select(driver.find_element_by_id("id_matrix_type")).select_by_visible_text("Matriz de escala de 1 al 10")
        driver.find_element_by_id("id_matrix_type").click()
        Select(driver.find_element_by_id("id_matrix_type")).select_by_visible_text("Matriz de escala de 3 caras")
        driver.find_element_by_id("id_matrix_type").click()
        Select(driver.find_element_by_id("id_matrix_type")).select_by_visible_text("Matriz de escala de 5 caras")
        driver.find_element_by_id("id_matrix_type").click()
        Select(driver.find_element_by_id("id_matrix_type")).select_by_visible_text("Matriz de escala de 5 estrellas")
        driver.find_element_by_id("id_scale_label").click()
        Select(driver.find_element_by_id("id_scale_label")).select_by_visible_text("Decepcionante / Sobresaliente")
        driver.find_element_by_id("id_scale_label").click()
        Select(driver.find_element_by_id("id_scale_label")).select_by_visible_text("Nunca / Siempre (5)")
        driver.find_element_by_id("id_scale_label").click()
        Select(driver.find_element_by_id("id_scale_label")).select_by_visible_text(u"Definitivamente no / Definitivamente sí")
        driver.find_element_by_id("id_scale_label").click()
        Select(driver.find_element_by_id("id_scale_label")).select_by_visible_text("Totalmente en desacuerdo / Totalmente de acuerdo")
        driver.find_element_by_id("id_scale_label").click()
        Select(driver.find_element_by_id("id_scale_label")).select_by_visible_text("Muy malo / Muy bueno")
        driver.find_element_by_id("id_scale_label").click()
        Select(driver.find_element_by_id("id_scale_label")).select_by_visible_text("Muy improbable / Muy probable")
        driver.find_element_by_id("id_scale_label").click()
        Select(driver.find_element_by_id("id_scale_label")).select_by_visible_text(u"Pésimo / Excelente")
        driver.find_element_by_id("id_scale_label").click()
        Select(driver.find_element_by_id("id_scale_label")).select_by_visible_text("Nada importante / Muy importante")
        driver.find_element_by_id("id_scale_label").click()
        Select(driver.find_element_by_id("id_scale_label")).select_by_visible_text("Nunca / Siempre (4)")
        driver.find_element_by_id("id_scale_label").click()
        Select(driver.find_element_by_id("id_scale_label")).select_by_visible_text("Siempre / Nunca (4)")
        driver.find_element_by_id("id_scale_label").click()
        Select(driver.find_element_by_id("id_scale_label")).select_by_visible_text("Decepcionante / Sobresaliente")
        driver.find_element_by_id("id_su_question_group_tpl").click()
        driver.find_element_by_id("submit_matrix").click()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("//div[@id='modal']/div/div/div/h4").click()
        driver.find_element_by_xpath("//div[@id='modal']/div/div/div/h4").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //div[@id='modal']/div/div/div/h4 | ]]
        driver.find_element_by_xpath("//div[@id='modal']/div/div/div/button/span").click()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("//div[@id='modal']/div/div/div/h4").click()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li[7]/a").click()
        driver.find_element_by_xpath("//div[@id='modal_history']/div/div/div/button/span").click()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li/a").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("dsfsdfsdf")
        driver.find_element_by_id("form_new_question_matrix_alternative").submit()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li/a").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("hola hola")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("//div[@id='modal']/div/div/div/button/span").click()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("//div[@id='modal']/div/div/div[2]/div/div/label/ul/li/a").click()
        driver.find_element_by_id("alertify-ok").click()
        driver.find_element_by_xpath("//div[@id='modal']/div/div/div/button/span").click()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li[5]/a").click()
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
