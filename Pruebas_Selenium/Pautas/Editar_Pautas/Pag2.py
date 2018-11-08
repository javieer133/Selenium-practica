# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains

import unittest, time, re, os

class NewPrueba(unittest.TestCase):

    path = os.path.dirname(os.path.realpath(__file__)).split("Pautas")[0]
    pdf_path = path + "Archivos\PDF\Mejoras Seguimiento.pdf"
    
    path = os.path.dirname(os.path.realpath(__file__)).split("Pautas")[0]
    imagen1_path = path + "Archivos\Image\satisfaccion-laboral-1.jpg"

    sistemaop = os.name
    if ("nt" not in sistemaop):
        imagen1_path = imagen1_path.replace("\\","/")
        print imagen1_path
        pdf_path = pdf_path.replace("\\","/")
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(2)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_new_prueba(self):
#La prueba para preguntas de seleccion se realiza primero con tipo lista, lugo se
#cambia  a multiple
        driver = self.driver
        print(self.imagen1_path)
        print(self.pdf_path)
        driver.get("https://qservus-qa.redcalidad.com/login/sign_in/")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("hector.sandoval.13@sansano.usm.cl")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("123456")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        
        driver.find_element_by_css_selector("span.fa.fa-list").click()

        lista = driver.find_elements_by_css_selector("a.list-group-item")#Lista con todas las pautas
        lista[len(lista)-9].click() # Click sobre la que quiero
        
        driver.find_element_by_css_selector("a.fa.fa-gear.pull-right").click()#Clickn sobre el engranaje
        driver.find_element_by_css_selector("span.fa.fa-edit").click()#Click sobre editar pauta
        driver.find_element_by_css_selector("span.fa.fa-2x.fa-arrow-right").click()#Click para pasar al custionario

        driver.find_element_by_xpath("//ul[@id='pautas_tab']/li[2]/a/span").click()#Seleccion de la hoja 2
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[4]/a").click()#Click sobre editar pregunta

        #cambiar tipo de pregunta a lista
        
        driver.find_element_by_id("id_su_question_type_id").click()
        Select(driver.find_element_by_id("id_su_question_type_id")).select_by_value("7")
        driver.find_element_by_id("id_su_question_type_id").click()
        
        
        #Cambiar enunciado
        self.editTitleSeleccion(driver)
        #Cambio del campo de texto de ayuda
        self.editHelpSeleccion(driver)
        #Cambio de la probabilidad de la pregunta
        self.editPorcentajeSeleccion(driver)
        
        #Cambio de tipo de pregunta a multiple
        tipo  = Select(driver.find_element_by_id("id_su_question_type_id"))
        antes = tipo.first_selected_option.get_attribute('value')#Obtencion del valor que posee el atributo
        driver.find_element_by_id("id_su_question_type_id").click()
        Select(driver.find_element_by_id("id_su_question_type_id")).select_by_value("3")
        driver.find_element_by_id("id_su_question_type_id").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[4]/a").click()
        segundo  = Select(driver.find_element_by_id("id_su_question_type_id"))
        despues = segundo.first_selected_option.get_attribute('value')
        print(despues)
        print(antes)
        try:
            assert antes != despues
        except:
            print("Error al cambiar tipo")
            driver.quit()

        #Cambio de opcione de orden
        self.editOrdenSeleccion(driver)
        #Cambio opcion de otros
        self.editOtrosSeleccion(driver)
        #Cambio del texto de opcion otros
        self.editTextOtrosSeleccion(driver)
        #Cambio del maximo
        self.editMaximoSeleccion(driver)
        #Cambio del minimo
        self.editMinimoSeleccion(driver)
        #Edicion de alternativas
        self.editTextAlternativaSeleccion(driver)
        self.editHelpAlternativaSeleccion(driver)
        #Alteracion de imagen
        self.editImagenSeleccion(driver)
        #Cambio de pagina
        self.editPaginaSeleccion(driver)
        
        driver.find_element_by_xpath("//button[@type='submit']").click()

########################################____Check___#############################################

        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div[2]/ul/li[2]/a").click()

        self.editTitle(driver)
        self.editPorcentaje(driver)
        self.editPage(driver)

        
        driver.find_element_by_xpath("//button[@type='submit']").click()

#################################____Terminos y condiciones____#####################################################

        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div[3]/ul/li[2]/a").click()
        self.editTitleTyC(driver)
        
        self.editPorcentajeTyC(driver)
        self.editPageTyC(driver)

        driver.find_element_by_id("id_question_attachment").send_keys(self.pdf_path)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        
######################################################################################

    def editTitleSeleccion(self,driver):
        #Cambio del atributo de enunciado de la pregunta
        titulo = driver.find_element_by_id("id_title")
        titulo.click()
        time.sleep(1)
        ant = titulo.get_attribute('value')
        titulo.send_keys("+")#Le agrego un signo de más al nombre que existe
        print(titulo.get_attribute('value'))#.encode('utf-8'))
        print(ant)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[4]/a").click()
        titulo = driver.find_element_by_id("id_title")
        time.sleep(1)
        try:
            assert titulo.get_attribute('value') != ant
        except:
            print("Error al editar el titulo")
        titulo.click()
        titulo.clear()
        titulo.send_keys('Seleccion')

#Editar Campo de ayuda
    def editHelpSeleccion(self,driver):
        ayuda = driver.find_element_by_id("id_help_text")
        ayuda.click()
        ant = ayuda.get_attribute('value')
        ayuda.send_keys("+")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[4]/a").click()
        ayuda = driver.find_element_by_id("id_help_text")
        print(ayuda.get_attribute('value'))#.encode('utf-8'))
        print(ant)
        try:
            assert ayuda.get_attribute('value') != ant
        except:
            print("Error al editar el Texto ayuda")
        ayuda.click()
        ayuda.clear()
        ayuda.send_keys('Help')

    def editPorcentajeSeleccion(self,driver):
        prioridad  = Select(driver.find_element_by_id("id_priority"))
        antes = prioridad.first_selected_option.get_attribute('value')
        driver.find_element_by_id("id_priority").click()
        if antes == '':
            antes = 0
        otrox = int(antes)%3 +1
        Select(driver.find_element_by_id("id_priority")).select_by_value(str(otrox))
        driver.find_element_by_id("id_priority").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[4]/a").click()
        segundo  = Select(driver.find_element_by_id("id_priority"))
        despues = segundo.first_selected_option.get_attribute('value')
        print(despues)
        print(antes)
        try:
            assert antes != despues
        except:
            print("Error al cambiar porcentaje")

    def editOrdenSeleccion(self,driver):
        old_orden = driver.find_element_by_name("random_order_alternatives").is_selected()
        print(old_orden)
        driver.find_element_by_xpath("//form[@id='form_question_selection']/div[2]/label").click()#Click sobre el check

        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[4]/a").click()
        
        new_orden = driver.find_element_by_name("random_order_alternatives").is_selected()
        print(new_orden)
        try:
            assert old_orden != new_orden
        except:
            print("Error al cambiar check de orden")

    def editOtrosSeleccion(self,driver):
        old_orden = driver.find_element_by_name("alternative_other").is_selected()
        print(old_orden)
        driver.find_element_by_xpath("//form[@id='form_question_selection']/div[3]/label").click()#Click sobre el check

        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[4]/a").click()
        
        new_orden = driver.find_element_by_name("alternative_other").is_selected()
        print(new_orden)
        try:
            assert old_orden != new_orden
        except:
            print("Error al cambiar check de Otros")

    def editTextOtrosSeleccion(self,driver):
        otro = driver.find_element_by_id("id_alternative_other_label")
        otro.click()
        antes = otro.get_attribute('value')
        otro.send_keys("+")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[4]/a").click()
        otro = driver.find_element_by_id("id_alternative_other_label")
        ahora = otro.get_attribute('value')
        print(ahora)
        print(antes)
        try:
            assert ahora != antes
        except:
            print("Error al editar el Texto de la alternativa Otros")
        otro.click()
        otro.clear()
        otro.send_keys('Help')

    def editMinimoSeleccion(self,driver):
        driver.find_element_by_id("id_min_selection").click()
        minimo  = driver.find_element_by_id("id_min_selection").get_attribute('value')
                
        driver.find_element_by_id("id_max_selection").click()#Aumentamos el maximo para que no salte el error
        driver.find_element_by_id("id_max_selection").send_keys("0")
        
        driver.find_element_by_id("id_min_selection").click()
        driver.find_element_by_id("id_min_selection").send_keys("1")
        new_minimo = driver.find_element_by_id("id_min_selection").get_attribute('value')
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[4]/a").click()

        print(minimo)
        print(new_minimo)
        try:
            assert minimo != new_minimo
        except:
            print("Error al cambiar minimo de respuestas")

        driver.find_element_by_id("id_min_selection").clear()
        driver.find_element_by_id("id_max_selection").clear()
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def editMaximoSeleccion(self,driver):
        driver.find_element_by_id("id_max_selection").click()
        maximo  = driver.find_element_by_id("id_max_selection").get_attribute('value')
        driver.find_element_by_id("id_max_selection").click()
        driver.find_element_by_id("id_max_selection").send_keys("1")
        new_maximo = driver.find_element_by_id("id_max_selection").get_attribute('value')
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[4]/a").click()

        print(maximo)
        print(new_maximo)
        try:
            assert maximo != new_maximo
        except:
            print("Error al cambiar maximo de respuestas")

    def editTextAlternativaSeleccion(self,driver):
        #driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_class_name('fa.fa-list-ol.modal-alternatives').click()
        driver.find_element_by_xpath("//div[@id='modal']/div/div/div[2]/div/div/label/ul/li[2]/a").click()
        #Cambio de enunciado alternativa
        alternativa = driver.find_element_by_id("id_name")
        alternativa.click()
        antes = alternativa.get_attribute('value')
        alternativa.send_keys("+")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        
        #driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_class_name('fa.fa-list-ol.modal-alternatives').click()
        driver.find_element_by_xpath("//div[@id='modal']/div/div/div[2]/div/div/label/ul/li[2]/a").click()

        segundo = driver.find_element_by_id("id_name")
        ahora = segundo.get_attribute('value')

        print(ahora)
        print(antes)
        try:
            assert ahora != antes
        except:
            print("Error al editar el Texto de la alternativa")

        segundo.clear()
        segundo.send_keys('Alternativa')

    def editHelpAlternativaSeleccion(self, driver):
        ayuda_alternativa = driver.find_element_by_id("id_help_text")
        ayuda_alternativa.click()
        antes = ayuda_alternativa.get_attribute('value')
        ayuda_alternativa.send_keys("+")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        #driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_class_name('fa.fa-list-ol.modal-alternatives').click()
        driver.find_element_by_xpath("//div[@id='modal']/div/div/div[2]/div/div/label/ul/li[2]/a").click()
        segundo = driver.find_element_by_id("id_help_text")
        ahora = segundo.get_attribute('value')
        print(ahora)
        print(antes)
        try:
            assert ahora != antes
        except:
            print("Error al editar el Texto de ayuda de la alternativa")
        segundo.clear()

    def editImagenSeleccion(self, driver):
        driver.find_element_by_id("id_image").send_keys(self.imagen1_path)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[4]/a").click()

    def editPaginaSeleccion(self, driver):
        pagina  = Select(driver.find_element_by_id("id_su_question_group_tpl"))
        antes = pagina.first_selected_option.text
        driver.find_element_by_id("id_su_question_group_tpl").click()
        Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']")).select_by_visible_text("Ultima")#cambiar valor 
        driver.find_element_by_id("id_su_question_group_tpl").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        try:
            driver.find_element_by_xpath("//div[@id='page_5']/div[2]/div/ul/li[4]/a").click()
        except:
            print("Error en cambio de pagina")
            driver.quit()
        segundo = Select(driver.find_element_by_id("id_su_question_group_tpl"))
        ahora = segundo.first_selected_option.text
        print(antes)
        print(ahora)
        try:
            assert antes != ahora
        except:
            print("Error al cambiar página")
        driver.find_element_by_id("id_su_question_group_tpl").click()
        Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']")).select_by_visible_text("Página 2") 
        driver.find_element_by_id("id_su_question_group_tpl").click()
    

###########################Funciones de Check##################################
        
    def editTitle(self,driver):
        driver.find_element_by_id("id_title").click() #Valor antes de editar
        valorAntes = driver.find_element_by_xpath("//*[@id='id_title']").get_attribute('value')

        driver.find_element_by_id("id_title").send_keys(" valor agregado")#Valor a sobreescribir al anterior
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div[2]/ul/li[2]/a").click()
        driver.find_element_by_id("id_title").click() #Nuevo valor
        ValorDespues =  driver.find_element_by_id("id_title").get_attribute('value')
        assert (valorAntes != ValorDespues), 'No se ha cambiado el valor'

    def editPorcentaje(self,driver):
        #Segmento de código utilizado para verificar si cambió el % de pregunta
        prioridad  = Select(driver.find_element_by_id("id_priority"))
        antes = prioridad.first_selected_option.get_attribute('value')
        driver.find_element_by_id("id_priority").click()
        if antes == '':
            antes = 0
        otrox = int(antes)%3 +1
        Select(driver.find_element_by_id("id_priority")).select_by_value(str(otrox))
        driver.find_element_by_id("id_priority").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div[2]/ul/li[2]/a").click()
        segundo  = Select(driver.find_element_by_id("id_priority"))
        despues = segundo.first_selected_option.get_attribute('value')
        assert (antes != despues), 'No se ha cambiado el valor'

    def editPage(self,driver):

        #Segmento de código utilizado para verificar si cambió la página
        driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']").click()
        page = Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']"))
        oldPage = page.first_selected_option.text
        Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']")).select_by_visible_text("Ultima")#cambiar valor
        driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        
        #driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div/ul/li[2]/a").click()#Actualiza la búsqueda del modal
        driver.find_element_by_xpath("//div[@id='page_5']/div[2]/div/ul/li[2]/a").click()

        driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']").click()
        page = Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']")) 
        newPage = page.first_selected_option.text
        assert (oldPage != newPage), 'No de ha cambiado de página'
        Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']")).select_by_visible_text("Página 2")
        
##################################################################################

    def editTitleTyC(self,driver):
        #Editar y comprobra el enunciado
        driver.find_element_by_id("id_title").click()
        #driver.find_element_by_id("id_title").clear()
        enunciadoAntes = driver.find_element_by_id("id_title").get_attribute('value')
        driver.find_element_by_id("id_title").send_keys("Pregunta 1")#editar pregunta 
       
        #driver.find_element_by_xpath("//*[@id='form_new_question']/div[1]/div[2]/div[2]/div").click()
        #driver.find_element_by_xpath("//*[@id='form_new_question']/div[1]/div[2]/div[2]/div").clear()
        driver.find_element_by_id("id_question_attachment").send_keys(self.pdf_path)
        driver.find_element_by_xpath("//button[@type='submit']").click()

        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div[3]/ul/li[2]/a").click()
        driver.find_element_by_id("id_title").click() #Nuevo valor
        enunciadoDespues =  driver.find_element_by_xpath("//*[@id='id_title']").get_attribute('value')
        assert (enunciadoAntes != enunciadoDespues), 'No se ha cambiado el valor'

    def editPorcentajeTyC(self,driver):
        #Segmento de código utilizado para verificar si cambió el % de pregunta
        
        prioridad  = Select(driver.find_element_by_id("id_priority"))
        antes = prioridad.first_selected_option.get_attribute('value')
        driver.find_element_by_id("id_priority").click()
        if antes == '':
            antes = 0
        otrox = int(antes)%3 +1
        Select(driver.find_element_by_id("id_priority")).select_by_value(str(otrox))
        driver.find_element_by_id("id_priority").click()
        driver.find_element_by_id("id_question_attachment").send_keys(self.pdf_path)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_2']/div[2]/div[3]/ul/li[2]/a").click()
        segundo  = Select(driver.find_element_by_id("id_priority"))
        despues = segundo.first_selected_option.get_attribute('value')
        assert (antes != despues), 'No se ha cambiado el valor'

    def editPageTyC(self,driver):
        #Segmento para ver si se cambio de página
        driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']").click()
        page = Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']"))
        oldPage = page.first_selected_option.text
        Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']")).select_by_visible_text("Ultima")#cambiar valor 
        driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']").click()
        driver.find_element_by_id("id_question_attachment").send_keys(self.pdf_path)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='page_5']/div[2]/div/ul/li[2]/a").click()#Actualiza la búsqueda del modal
        driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']").click()
        page = Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']")) 
        newPage = page.first_selected_option.text
        assert (oldPage != newPage), 'No de ha cambiado de página'
        Select(driver.find_element_by_xpath("//*[@id='id_su_question_group_tpl']")).select_by_visible_text("Página 2")

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
