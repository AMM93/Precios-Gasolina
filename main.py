# https://sedeaplicaciones.minetur.gob.es/shpcarburantes/

# Import libraries
import pandas as pd
import numpy as np
from datetime import date
from scrap_functions import *

url = "https://sedeaplicaciones.minetur.gob.es/shpcarburantes/"
webdriver = scrap(url)


# Qué queremos sacar y cómo
temporalidad = ['Diaria', 'Semanal', 'Mensual', 'Anual']


# Consultamos histórico de precios

tipo_temporal = '/html/body/form/div[3]/div[3]/div/div[1]/fieldset[1]/div[2]/select'

webdriver.pick_temporalidad('Mensual')









