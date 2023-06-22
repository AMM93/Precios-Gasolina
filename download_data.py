# https://sedeaplicaciones.minetur.gob.es/shpcarburantes/


# Import libraries
import pandas as pd
import numpy as np
from datetime import date
from scrap_functions import *
import shutil
from datetime import date, timedelta
import os

year = 2023 # Write an specific year of study or origin date from starting download data

last_data = True # True in case we want the last data of the actual year
                 # False in case we want data from an specific year 


while year <= 2023:
                     
    #### To download the last data of this year (it has to be the day before today) ###
    if last_data == True:
        
        yesterday = date.today() - timedelta(days=1)
        data = yesterday.strftime('%d/%m/%Y')


    ### To download data for a certain year ###
    
    else:

        data = '31/12/' + str(year)

    url = "https://sedeaplicaciones.minetur.gob.es/shpcarburantes/"
    webdriver = scrap(url)


    ### Insertar Temporalidad ###
    webdriver.pick_temporalidad('Mensual')

    ### Insertar Tiempo Inicial y Final ###
    #
    webdriver.insert_dates('01/01/' + str(year), data)

    ## Insertar la busqueda con detalles
    webdriver.variables_to_plot(['Gasolinera', 'Madrid', 'Madrid', 'Madrid', 'Madrid', 'Alcampo', 'Gasolina 98 E5', 'G'])

    # Aceptar la busqueda
    webdriver.click_element('/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div/div[3]/fieldset/div[2]/input')

    # Descargar el Excel
    webdriver.click_element('/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div[1]/div[1]/div/table/tbody/tr[2]/td[5]/input[2]')

    # Renombrar y mover a la carpeta de source deseada. Siempre se guarda con nombre Data.xls
    file = '/Users/amm/Downloads/Datos.xls'
    
    new_file = str(year) + '.xls'
    
    #os.rename(file,"/Users/amm/Documents/Github/Data/Gasolina/source/Madrid_alcampo_gasolina_98_E5/" + new_file)
    #shutil.move(file, "/Users/amm/Documents/Github/Data/Gasolina/source/Madrid_alcampo_gasolina_98_E5/" + new_file)
    year+=1











