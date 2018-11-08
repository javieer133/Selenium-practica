# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class EditarCheckList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qservus-qa.redcalidad.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_editar_check_list(self):
        driver = self.driver
        driver.get(self.base_url + "/login/sign_in/")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("javier.154_@hotmail.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("practica_qservus")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_xpath("//li[@id='surveys']/a/span").click()
        #Segmento de código utilizado para verificar si cambió el enunciado de la pregunta
        driver.find_element_by_xpath("//ul[@id='entries']/li[17]/a/h2").click()#Selección de pauta, la primera es li[2]
        driver.find_element_by_xpath("//div[@id='toolbar']/a").click()
        driver.find_element_by_id("id_edit").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        #Hay que validar que el modal se encuentre en la página
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li[2]/a").click()#Botón editar
        self.editTitle(driver)
        self.editPorcentaje(driver)
        self.editPage(driver)

    def editTitle(self,driver):
        driver.find_element_by_id("id_title").click() #Valor antes de editar
        valorAntes = driver.find_element_by_xpath("//*[@id='id_title']").get_attribute('value')

        driver.find_element_by_id("id_title").send_keys(" valor agregado")#Valor a sobreescribir al anterior
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_id("id_title").click() #Nuevo valor
        ValorDespues =  driver.find_element_by_id("id_title").get_attribute('value')
        assert (valorAntes != ValorDespues), 'No se ha cambiado el valor'

    def editPorcentaje(self,driver):
        #Segmento de código utilizado para verificar si cambió el % de pregunta
        driver.find_element_by_id("id_priority").click()
        porcentaje = Select(driver.find_element_by_id("id_priority"))
        antes = porcentaje.first_selected_option.text
        Select(driver.find_element_by_id("id_priority")).select_by_visible_text("50%")#cambiar valor
        driver.find_element_by_id("id_priority").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_id("id_priority").click()
        porcentaje = Select(driver.find_element_by_id("id_priority"))
        despues = porcentaje.first_selected_option.text
        assert (antes != despues), 'No se ha cambiado el valor'

    def editPage(self,driver):

        #Segmento de código utilizado para verificar si cambió la página
        driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']").click()
        page = Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']"))
        oldPage = page.first_selected_option.text
        Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']")).select_by_visible_text("Pagina 2")#cambiar valor 
        driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[2]/a").click()#Actualiza la búsqueda del modal
        driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']").click()
        page = Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']")) 
        newPage = page.first_selected_option.text
        assert (oldPage != newPage), 'No de ha cambiado de página'



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
