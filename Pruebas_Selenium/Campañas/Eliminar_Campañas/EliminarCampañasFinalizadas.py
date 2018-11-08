# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import os



import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TerminarDeCrearCampanas(unittest.TestCase):

    current_path = os.path.dirname(os.path.realpath(__file__))
    doc_path = current_path.split("testing/Pruebas")[0]
    doc_path = doc_path + "testing/Pruebas_Selenium/Archivos/VariableParaEvitarBorrar.txt"
    print(doc_path)
    file = open (doc_path,"r")
    skip = file.read()
    file.close()


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qservus-qa.redcalidad.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_terminar_de_crear_campanas(self):
        driver = self.driver
        driver.get(self.base_url + "/login/sign_in/")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("miguel.antonio.bono@gmail.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("practica_qservus")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        #Fin de login
        driver.find_element_by_css_selector("span.fa.fa-bullhorn").click()



        list_number = 2
        while True:
            driver.find_element_by_id("filter_btn").click()
            driver.find_element_by_xpath("//ul[@id='menu1']/li[3]/a/span[2]").click()
            try:
                current_campaign = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[{}]/a/h2".format(list_number)).text 
                if(current_campaign == "Crear nueva campaña"):
                    print("La lista de campañas esta vacia, no hay nada por eliminar...")
                    break
            except:

                print("No se puede continuar eliminando campañas finalizadas, posiblemente ya no quedan...")
                break

            if(current_campaign.find(self.skip) == -1):
###########3
        



                print("Eliminando campaña en ejecucion --->" + current_campaign)
                driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[{}]/a/h2".format(list_number)).click()
                driver.find_element_by_id("options").click()
                actions = driver.find_element_by_css_selector(".dropdown-submenu > a:nth-child(1) > span:nth-child(2)")
                hover = ActionChains(driver).move_to_element(actions)
                hover.perform()   


                driver.find_element_by_css_selector("#delete_campaign > span:nth-child(2)").click()
                driver.find_element_by_id("alertify-ok").click()
                print("      Campaña {} eliminada con exito".format(current_campaign))
############

                


            else:
                print("Esta campaña no fue modificada --->" + current_campaign)
                list_number = list_number + 1


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
