# https://sedeaplicaciones.minetur.gob.es/shpcarburantes/

# Import libraries
import pandas as pd
import numpy as np
from datetime import date
from scrap_functions import *

url = "https://sedeaplicaciones.minetur.gob.es/shpcarburantes/"
webdriver = scrap(url)

### Insertar Temporalidad ###
webdriver.pick_temporalidad('Mensual')

### Insertar Tiempo Inicial y Final ###
webdriver.insert_dates('20/03/2021', '20/03/2022')

## Insertar la busqueda con detalles
webdriver.variables_to_plot(['Gasolinera', 'Madrid', 'Madrid', 'Madrid', 'Madrid', 'Alcampo', 'Gasolina 98 E5', 'G'])

# Aceptar la busqueda
webdriver.click_element('/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div/div[3]/fieldset/div[2]/input')

# Descargar el Excel
webdriver.click_element('/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div[1]/div[1]/div/table/tbody/tr[2]/td[5]/input[2]')










