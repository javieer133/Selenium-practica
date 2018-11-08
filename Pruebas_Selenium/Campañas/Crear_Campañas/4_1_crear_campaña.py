# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class 4_1_crear_campaña(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://qservus-ppr.redcalidad.com/newsfeed/")
        self.selenium.start()
    
    def test_4_1_crear_campaña(self):
        sel = self.selenium
        sel.open("/newsfeed/")
        sel.click("css=span.fa.fa-bullhorn")
        sel.wait_for_page_to_load("30000")
        sel.click("id=new-camp")
        sel.wait_for_page_to_load("30000")
        sel.type("id=id_name", "Selenium")
        sel.select("id=id_su_survey", "label=Selenium")
        sel.type("id=id_email_subject", "Selenium_Test_automated")
        sel.click("id=show_hide_options")
        sel.click("id=create_campaign")
        sel.wait_for_page_to_load("30000")
        sel.click("css=#add_recipients_1 > a.list-group-item > p.bajada")
        sel.wait_for_page_to_load("30000")
        sel.type("id=name_simple", "Daniel Hebel Lobos")
        sel.type("id=email_simple", "daniel.hebel@sansano.usm.cl")
        sel.click("id=add_simple")
        sel.click("name=checkbox")
        sel.click("id=send_test")
        sel.click("//div[@id='toolbar']/a[2]")
        sel.wait_for_page_to_load("30000")
        sel.click("css=#init_campaign_2 > p.bajada")
        sel.click("id=alertify-ok")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
