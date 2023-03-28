# https://sedeaplicaciones.minetur.gob.es/shpcarburantes/

# Import libraries
import pandas as pd
import numpy as np
from datetime import date
from scrap_functions import *
import shutil

#### Select year to download ###
year = '2023'
url = "https://sedeaplicaciones.minetur.gob.es/shpcarburantes/"
webdriver = scrap(url)

### Insertar Temporalidad ###
webdriver.pick_temporalidad('Mensual')

### Insertar Tiempo Inicial y Final ###
#webdriver.insert_dates('01/01/' + year, '31/12/' + year)
webdriver.insert_dates('01/01/' + year, '27/03/' + year)

## Insertar la busqueda con detalles
webdriver.variables_to_plot(['Gasolinera', 'Madrid', 'Madrid', 'Madrid', 'Madrid', 'Alcampo', 'Gasolina 98 E5', 'G'])

# Aceptar la busqueda
webdriver.click_element('/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div/div[3]/fieldset/div[2]/input')

# Descargar el Excel
webdriver.click_element('/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div[1]/div[1]/div/table/tbody/tr[2]/td[5]/input[2]')

# Renombrar y mover a la carpeta de source deseada. Siempre se guarda con nombre Data.xls
file = '/Users/amm/Downloads/Datos.xls'
new_file = year + '.xls'
shutil.move(file, "/Users/amm/Documents/Github/Data/Gasolina/source/Madrid, alcampo, gasolina 98_E5/" + new_file)











