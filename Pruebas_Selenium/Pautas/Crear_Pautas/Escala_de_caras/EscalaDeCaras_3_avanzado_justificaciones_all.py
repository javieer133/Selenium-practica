# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class EscalaDeCaras3AvanzadoJustificacionSatisfaccion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_escala_de_caras3_avanzado_justificacion_satisfaccion(self):
        driver = self.driver
        driver.get("https://qservus-qa.redcalidad.com/login/sign_in/")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("marcelo.rivera.contreras@gmail.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("practica_qservus")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_css_selector("span.fa.fa-list").click()
        driver.find_element_by_id("template_new").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("Pauta de prueba")
        driver.find_element_by_css_selector("button.btn.btn-success.pull-right").click()
        driver.find_element_by_css_selector("a.add-scale-modal > span.label").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("Enunciado de la pregunta")
        driver.find_element_by_id("show_hide_options").click()
        driver.find_element_by_id("id_justification_type").click()
        Select(driver.find_element_by_id("id_justification_type")).select_by_visible_text(u"Nota de satisfacción e insatisfacción")
        driver.find_element_by_id("id_justification_type").click()
        driver.find_element_by_css_selector("div.botonera.clearfix > button.btn.btn-success.pull-right").click()
        driver.find_element_by_css_selector("a.add-scale-modal > span.label").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("Enunciado de la pregunta")
        driver.find_element_by_css_selector("#show_hide_options > span").click()
        driver.find_element_by_id("id_justification_type").click()
        Select(driver.find_element_by_id("id_justification_type")).select_by_visible_text("Justificar en todas las notas")
        driver.find_element_by_id("id_justification_type").click()
        driver.find_element_by_css_selector("div.botonera.clearfix > button.btn.btn-success.pull-right").click()
        driver.find_element_by_css_selector("a.add-scale-modal > span.label").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("Enunciado de la pregunta")
        driver.find_element_by_id("show_hide_options").click()
        driver.find_element_by_id("id_justification_type").click()
        Select(driver.find_element_by_id("id_justification_type")).select_by_visible_text(u"Solo notas distintas a la máxima")
        driver.find_element_by_id("id_justification_type").click()
        driver.find_element_by_css_selector("div.botonera.clearfix > button.btn.btn-success.pull-right").click()
        driver.find_element_by_css_selector("a.add-scale-modal > span.label").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("Enunciado de la pregunta")
        driver.find_element_by_id("show_hide_options").click()
        driver.find_element_by_id("id_justification_type").click()
        Select(driver.find_element_by_id("id_justification_type")).select_by_visible_text(u"Notas distintas a las de satisfacción")
        driver.find_element_by_id("id_justification_type").click()
        driver.find_element_by_css_selector("div.botonera.clearfix > button.btn.btn-success.pull-right").click()
        driver.find_element_by_css_selector("span.fa.fa-3x.fa-save").click()
    
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
