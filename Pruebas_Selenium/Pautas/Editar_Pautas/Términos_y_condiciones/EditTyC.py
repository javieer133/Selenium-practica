# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os

class EditTyC(unittest.TestCase):
    path = os.path.dirname(os.path.realpath(__file__)).split("/Pauta")[0]
    pdf_path = path + "/Archivos/PDF/Mejoras Seguimiento.pdf"
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qservus-qa.redcalidad.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    
    def test_edit_ty_c(self):
        driver = self.driver
        driver.get(self.base_url + "/login/sign_in/")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("javier.154_@hotmail.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("practica_qservus")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_xpath("//li[@id='surveys']/a/span").click()
        driver.find_element_by_xpath("//ul[@id='entries']/li[2]/a/h2").click()
        driver.find_element_by_xpath("//div[@id='toolbar']/a").click()
        driver.find_element_by_id("id_edit").click()
        driver.find_element_by_xpath("//form[@id='survey_template_create']/div").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li[2]/a").click()
        self.editTitle(driver)    
        self.editPorcentaje(driver)
        self.editPage(driver)

    def editTitle(self,driver):
        #Editar y comprobra el enunciado
        driver.find_element_by_id("id_title").click()
        #driver.find_element_by_id("id_title").clear()
        enunciadoAntes = driver.find_element_by_id("id_title").get_attribute('value')
        driver.find_element_by_id("id_title").send_keys("Pregunta 1")#editar pregunta 
       
        #driver.find_element_by_xpath("//*[@id='form_new_question']/div[1]/div[2]/div[2]/div").click()
        #driver.find_element_by_xpath("//*[@id='form_new_question']/div[1]/div[2]/div[2]/div").clear()
        driver.find_element_by_id("id_question_attachment").send_keys(self.pdf_path)
        driver.find_element_by_xpath("//button[@type='submit']").click()

        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_id("id_title").click() #Nuevo valor
        enunciadoDespues =  driver.find_element_by_xpath("//*[@id='id_title']").get_attribute('value')
        assert (enunciadoAntes != enunciadoDespues), 'No se ha cambiado el valor'

    def editPorcentaje(self,driver):
        #Segmento de código utilizado para verificar si cambió el % de pregunta
        driver.find_element_by_id("id_priority").click()
        porcentaje = Select(driver.find_element_by_id("id_priority"))
        antes = porcentaje.first_selected_option.text
        Select(driver.find_element_by_id("id_priority")).select_by_visible_text("100%")#cambiar valor
        driver.find_element_by_id("id_priority").click()
        driver.find_element_by_id("id_question_attachment").send_keys(self.pdf_path)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_1']/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_id("id_priority").click()
        porcentaje = Select(driver.find_element_by_id("id_priority"))
        despues = porcentaje.first_selected_option.text
        assert (antes != despues), 'No se ha cambiado el valor'

    def editPage(self,driver):
        #Segmento para ver si se cambio de página
        driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']").click()
        page = Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']"))
        oldPage = page.first_selected_option.text
        Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']")).select_by_visible_text("Pagina 2")#cambiar valor 
        driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']").click()
        driver.find_element_by_id("id_question_attachment").send_keys(self.pdf_path)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[4]/a").click()#Actualiza la búsqueda del modal
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
