# https://sedeaplicaciones.minetur.gob.es/shpcarburantes/

# Import libraries
import pandas as pd
import numpy as np
from datetime import date
from scrap_functions import *

url = "https://sedeaplicaciones.minetur.gob.es/shpcarburantes/"
webdriver = scrap(url)

webdriver.write_in_box("/html/body/form/div[3]/div[3]/div/div[1]/fieldset[1]/div[3]/input", "01/09/2021")





