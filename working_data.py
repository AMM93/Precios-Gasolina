import pandas as pd
import numpy as np
import glob
from datetime import datetime
import plotly.express as px
import seaborn as sns
import xgboost as xgb


input = "/Users/amm/Documents/Github/Data/Gasolina/source/Madrid, alcampo, gasolina 98_E5/"
files = glob.glob(input + '*.xls')

df = pd.concat([pd.read_excel(file) for file in files], ignore_index=True)

df['Fecha'] = pd.to_datetime(df['Fecha'])
df.sort_values(by='Fecha', inplace = True)

fig = px.line(df, x = 'Fecha', y = 'Precio', title = 'Gasolina 98 E5 Madrid 2020 - 2023')
fig.show()
df
