# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import os
from datetime import datetime, date, timedelta
import unittest, time, re

class CampaACrear1(unittest.TestCase):

    ##########  CAMBIAR AQUI EL ARCHIVO EXCEL ############
    ######################################################
    xlsx_name = "Botsito-testing.xlsx"
    ######################################################
    ######################################################

    

    extract_path = os.path.dirname(os.path.realpath(__file__))
    project_folder = (extract_path.split("/Campaña"))[0]
    now = datetime.now()
    time_now = "("+str(now.day) + "."+str(now.month)+"."+str(now.year)+")"


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://qservus-qa.redcalidad.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_campa_a_crear1(self):
        print("{}/Archivos/XLSX/{}".format(self.project_folder,self.xlsx_name))
        driver = self.driver
        driver.get(self.base_url + "/login/sign_in/")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("miguel.antonio.bono@gmail.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("practica_qservus")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        #Fin de login
        driver.find_element_by_css_selector("span.fa.fa-list").click()
        driver.find_element_by_css_selector("h2.title").click()
        driver.find_element_by_xpath("//ul[@id='pautas_detalle_tab']/li[2]/a/span[2]").click()
        driver.find_element_by_css_selector("h2.title").click()
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"Campaña automatica-"+self.time_now)
        driver.find_element_by_id("id_email_subject").click()
        driver.find_element_by_id("id_email_subject").clear()
        driver.find_element_by_id("id_email_subject").send_keys(u"Campaña automatica-"+self.time_now)
        driver.find_element_by_id("create_campaign").click()
        driver.find_element_by_css_selector("#add_recipients_1 > a.list-group-item > p.bajada").click()
        driver.find_element_by_id("tab_file").click()
        #driver.find_element_by_id("id_recipients").click()
        driver.find_element_by_id("id_recipients").clear()
        driver.find_element_by_id("id_recipients").send_keys("{}/Archivos/XLSX/{}".format(self.project_folder,self.xlsx_name))
        driver.find_element_by_css_selector("button.btn.btn-success.pull-right").click()
        time.sleep(2)
        driver.find_element_by_css_selector("a.pull-left.fa.fa-2x.fa-arrow-left").click()
        driver.find_element_by_css_selector("#init_campaign_2 > p.bajada").click()
        driver.find_element_by_id("alertify-ok").click()
    
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
