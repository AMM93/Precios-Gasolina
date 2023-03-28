import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb

df = pd.read_excel('/Users/amm/Downloads/Datos.xls')
df = df.set_index('Fecha')
df.plot(style='.', figsize=(15, 5), )

