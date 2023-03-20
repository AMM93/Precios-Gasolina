# https://sedeaplicaciones.minetur.gob.es/shpcarburantes/

# Import libraries

from webdriver_manager.chrome import ChromeDriverManager
from time import sleep, strftime
from random import randint
import pandas as pd
import numpy as np
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class scrap():

    def __init__(self,url, wdriver = None) -> None:
        #options = Options()
        #options.add_argument('--headless')
        #options.add_argument('--disable-gpu')
        #wdriver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)
        self.wdriver = webdriver.Chrome(ChromeDriverManager().install())
        self.wdriver.get(url)

    
    def click_element(self, url):
        '''
        Funcion para reutilizar la funcion de selenium para hacer click un elemento dentro de la pagina web.
        Por tanto, clickea sobre un elemento y no esperamos nada de retorno

        Parameters
        ----------
        url: string
            xpath copiado del elemento de la página web que queremos encontrar
        '''
        
        return self.wdriver.find_element("xpath", url).click()
    
 
    def write_in_box(self, url, text):
        '''
        Funcion para escribir sobre un box que tengamos localizado.

        Parameters
        ----------
        box: es un click_element() del objeto webdriver creado en este fichero
        text: lo que queramos que escriba en dicha box
        '''
        #breath(1,1)
        a = self.click_element(url)
        a.send_keys(text)
        
    def get_text(self):
        '''
        Funcion para reutilizar la funcion de selenium para leer el texto de un elemento dentro de la pagina web.

        Parameters
        ----------
        url: string
            xpath copiado del elemento de la página web que queremos encontrar
        
        Returns
        -------
        string
            Devuelve el texto que queríamos extraer de la web
        
        '''
        #breath(2,3)
        return webdriver.find_element("xpath", self).text
    
    def pick_temporalidad(self, freq_temporal):
        '''
        Funcion para decidir con qué frecuencia sacamos los datos.

        Parameters
        ----------
        freq_temporal: string
            Opciones: Diaria, Semanal, Mensual, Anual
        '''
        print(freq_temporal)
        if freq_temporal == 'Diaria':
            i = 0
        if freq_temporal == 'Semanal':
            i = 1
        if freq_temporal == 'Mensual':
            i = 2
        if freq_temporal == 'Anual':
            i = 3
        else:
            print("Frecuencia añadida incorrecta, por favor, revisa lo introducido")
               
        print(i)            
        return self.click_element(f"/html/body/form/div[3]/div[3]/div/div[1]/fieldset[1]/div[2]/select/option[{i}]")

