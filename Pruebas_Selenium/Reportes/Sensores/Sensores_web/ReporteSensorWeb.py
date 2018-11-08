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
        driver.find_element_by_xpath("(//a[@id=''])[2]").click()
        driver.find_element_by_xpath("//div[@id='content']/div[3]/div/ul/li[4]/a/p").click() #Acá se elige el Sensor
        driver.find_element_by_xpath("//div[@id='content']/ul/li[4]/a/h2").click()#Acá se elige si es PDF o cualquier otro tipo(Web defecto)
        try:
            driver.switch_to.window(self.driver.window_handles[1])
        except:
            print("No se pudo generar el reporte")
        if driver.find_element_by_tag_name('h3').text == "La página que está buscando no puede ser encontrada.":
            print("No se encuentra el reporte")
        elif driver.find_element_by_tag_name('h3').text == "No tienes acceso a esta sección" :
            print("no existen permisos para ver el reporte")
        else:
            print("Reporte generado.")
            time.sleep(5)
            self.verificarFiltros(driver)
            self.limpiarFiltros(driver)


    def verificarFiltros(self,driver):
        valueAntes = driver.find_element_by_id("id_range_date").get_attribute('value')
        driver.find_element_by_id("id_range_date").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[1]").click() #cambio de filtro, en este caso corresponde a hoy
        valueDespues = driver.find_element_by_id("id_range_date").get_attribute('value')
        try:
            assert valueAntes == valueDespues
            print("No hay cambio")
        except:
            driver.find_element_by_xpath("//*[@id='web_report_filter']/div[2]/button[2]").click()
            print("antes: ",valueAntes)
            print("despues: ",valueDespues)
            print("Funciona el filtro")
            print("***********************************************")

    def limpiarFiltros(self,driver):
        valueAntes = driver.find_element_by_id("id_range_date").get_attribute('value')
        driver.find_element_by_id("id_range_date").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[2]").click() #ayer
        pibote = driver.find_element_by_id("id_range_date").get_attribute('value')
        driver.find_element_by_xpath("//*[@id='reset_filters']").click()
        valueDespues = driver.find_element_by_id("id_range_date").get_attribute('value')
        print("antes: ",valueAntes)
        print("pibote: ",pibote)
        print("despues: ",valueDespues)
        print("\n")
        try:
            assert valueAntes != valueDespues
            print("no se reestableció el filtro")
        except:
            print("Se limpió el filtro.")

    
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
