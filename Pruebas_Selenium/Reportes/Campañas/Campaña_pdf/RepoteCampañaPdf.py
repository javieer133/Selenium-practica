# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ReporteSensorPdf(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "https://qservus-qa.redcalidad.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_reporte_sensor_pdf(self):
        driver = self.driver
        driver.get(self.base_url + "/login/sign_in/")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("javier.154_@hotmail.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("practica_qservus")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        #*****#
        
        driver.find_element_by_xpath("//li[@id='reports_menu']/a/span").click()
        driver.find_element_by_xpath("(//a[@id=''])[1]").click()
        driver.find_element_by_xpath("//div[@id='content']/div[3]/div/ul/li[2]/a/p").click() #Acá se elige la campaña
        driver.find_element_by_xpath("//ul[@id='list_campaigns']/li/a/h2").click() #Acá se elige si es PDF o cualquier otro tipo(PDF defecto)
        try: 
            driver.switch_to.window(self.driver.window_handles[1])
            try:
                driver.find_element_by_tag_name('h3')
                if driver.find_element_by_tag_name('h3').text == "La página que está buscando no puede ser encontrada.":
                    print("No se encuentra el reporte")
                elif driver.find_element_by_tag_name('h3').text == "No tienes acceso a esta sección" :
                    print("no existen permisos para ver el reporte")
            except:
                print("Funciona Ok.")
        except:
            print("Error.")

    
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
