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
webdriver.insert_dates('01/01/2023', '20/03/2023')






