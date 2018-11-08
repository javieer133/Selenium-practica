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
        driver.find_element_by_xpath("//ul[@id='entries']/li[3]/a/p").click()
        driver.find_element_by_xpath("//div[@id='content']/div[3]/div/ul/li[2]/a/p").click() #Acá se elige la Pauta
        driver.find_element_by_xpath("//div[@id='content']/div[3]/div/ul/li[2]/a").click()#Acá se elige si es PDF o cualquier otro tipo(Web defecto)
        time.sleep(5)
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
            self.verificarFiltroFecha(driver)
            self.verificarFiltroPregunta(driver)
            #self.verificarFiltroCampaña(driver)
            self.limpiarFiltros(driver)


    def verificarFiltroFecha(self,driver):
        time.sleep(2)
        valueAntes = driver.find_element_by_xpath("//*[@id='id_range_date']").get_attribute('value')
        driver.find_element_by_id("id_range_date").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[2]").click() #cambio de filtro, en este caso corresponde a hoy
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

    #def verificarFiltroCampaña(self,driver):
    def verificarFiltroPregunta(self,driver):
        valorSelect = Select(driver.find_element_by_xpath("//*[@id='id_question_tpl']"))
        valueAntes = valorSelect.first_selected_option.get_attribute('value')
        lenghtOptions = driver.execute_script("return document.getElementsByClassName('form-control')[3].options.length;")
        if lenghtOptions < 2 :
            print("No hay preguntas")
            print("***********************************************")
        else:
            valueFirstOption = driver.execute_script("var selected = document.getElementsByClassName('form-control')[3]; return selected.options[1].value")
            if valueAntes == "":
                valueAntes = int(valueFirstOption) - 1
            cast = int(valueFirstOption)
            Select(driver.find_element_by_xpath("//*[@id='id_question_tpl']")).select_by_value(str(cast))
            valorSelect2 = Select(driver.find_element_by_xpath("//*[@id='id_question_tpl']"))
            valueDespues = valorSelect2.first_selected_option.get_attribute('value')
            try:
                assert valueAntes == valueDespues
                print("No hay cambio")
                print("***********************************************")
            except:
                driver.find_element_by_xpath("//*[@id='web_report_filter']/div[2]/button[2]").click()
                print("antes: ",valueAntes)
                print("despues: ",valueDespues)
                print("Funciona el filtro")
                print("***********************************************")

    #Este método sólo muestra que limpia las fechas
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
