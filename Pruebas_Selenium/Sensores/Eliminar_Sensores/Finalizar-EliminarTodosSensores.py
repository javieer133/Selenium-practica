# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import os

class EliminarSensor(unittest.TestCase):


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
    
    def test_eliminar_sensor(self):
        #Login
        driver = self.driver
        driver.get("https://qservus-qa.redcalidad.com/login/sign_in/")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("miguel.antonio.bono@gmail.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("practica_qservus")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        
        #Ir a la seccion sensores
        driver.find_element_by_css_selector("span.fa.fa-qrcode").click()
        
        #Variables auxiliares
        finalizo=0
        finalizar_while=True         
        
        ###Seleccionar el primer sensor y finalizarlo###
        #Si encuentro un sensor (primero) realizar todo esto
        
        list_number = 2
        while(finalizar_while):
            #Seleccionar filtro y seleccionar en ejecucion
            driver.find_element_by_id("filter_selector").click()
            driver.find_element_by_xpath("//ul[@id='menu2']/li/a/span[1]").click()
            try:
                #Obtengo el primer sensor y guardo su titulo para mostrarlo
                sensor=driver.find_element_by_css_selector("#entries > li:nth-child({}) > a > h2".format(list_number))
                titulo_sensor = sensor.text


                if(titulo_sensor.find(self.skip) == -1):
                    print("Finalizando senror    --> "+titulo_sensor)
                    #Selecciono dicho sensor
                    driver.find_element_by_css_selector("#entries > li:nth-child({}) > a > h2".format(list_number)).click()
                    
                    #Dentro de las opciones (engranaje), selecciono finalizar sensor y confirmar la operacion
                    driver.find_element_by_id("sensor_options").click()
                    driver.find_element_by_css_selector("#finish_sensor > span.padding-drop").click()
                    driver.find_element_by_id("alertify-ok").click()
                    driver.find_element_by_css_selector("a.pull-left.fa.fa-2x.fa-arrow-left").click()
                    print("Se ha finalizado el sensor:     "+titulo_sensor)
                    finalizo=1
                else:
                    list_number = list_number + 1
                    print("El Sensor '{}' no se ha modificado".format(titulo_sensor))
                
            except NoSuchElementException:
                finalizar_while=False
                
        if(finalizo==1):
            print ("Todas los sensores en ejecución se han finalizado")
        else:
            print("No se encontraron sensores en ejecución")
        
         #Volver a la seccion sensores
        #driver.find_element_by_css_selector("span.fa.fa-qrcode").click()
        driver.get("https://qservus-qa.redcalidad.com/sensors/")        
        #Actualizo variable condicional del while
        finalizar_while=True        
        

        list_number = 2
        while(finalizar_while):
            #Seleccionar filtro y seleccionar finalizados
            driver.find_element_by_id("filter_selector").click()
            driver.find_element_by_xpath("//ul[@id='menu2']/li[2]/a/span[2]").click()

            try:
                #Obtengo el primer sensor y guardo su titulo para mostrarlo
                sensor=driver.find_element_by_xpath("//*[@id='entries']/li[{}]".format(list_number))
                titulo_sensor = sensor.find_element_by_css_selector("h2")
                titulo_sensor = titulo_sensor.text
                #Selecciono dicho sensor

                if(titulo_sensor.find(self.skip) == -1):

                    sensor.find_element_by_css_selector("p.bajada").click()
                    #Dentro de las opciones (engranaje), selecciono finalizar sensor y confirmar la operacion
                    driver.find_element_by_id("sensor_options").click()
                    driver.find_element_by_css_selector("span.padding-drop").click()
                    driver.find_element_by_id("alertify-ok").click()
                    print("Se ha eliminado el sensor:"+titulo_sensor)
                else:
                    print("El Sensor '{}' no se ha modificado".format(titulo_sensor))
                    list_number = list_number + 1
                
            except NoSuchElementException:
                finalizar_while=False
                all_finalizated=1
                
                if(all_finalizated==1):
                    print ("Todas los sensores finalizadas se han eliminado")
                else:
                    print("No se encontraron sensores finalizados")
        
        
        '''
        while(index_inicial):
            
            a=driver.find_element_by_xpath("//*[@id='entries']/li["+str(index)+"]")
            b = a.find_element_by_css_selector("h2")
        '''
    


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
    unittest.main(exit=False)
