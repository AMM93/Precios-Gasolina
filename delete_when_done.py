import pandas as pd
import numpy as np
import glob
from datetime import datetime
import plotly.express as px
import seaborn as sns
import xgboost as xgb

# Leer y gather data
input = "/Users/amm/Documents/Github/Data/Gasolina/source/Madrid_alcampo_gasolina_98_E5/"
files = glob.glob(input + '*.xls')

df = pd.concat([pd.read_excel(file) for file in files], ignore_index=True)

df['Fecha'] = pd.to_datetime(df['Fecha'])
df.sort_values(by='Fecha', inplace = True)

fig = px.line(df, x = 'Fecha', y = 'Precio', title = 'Gasolina 98 E5 Madrid 2020 - 2023')
fig.show()

#########--------------------------#########
## Data Engineer

def create_features(df):
    '''
    Crearemos features de time series basados en el index para estudiar luego su comportamiento
    '''
    
    df = df.set_index('Fecha')
    df['month'] = df.index.month
    df['year'] = df.index.year
    
    return df

df_study = create_features(df)
fig = px.box(df_study, x= "month", y="Precio")
fig.show()

# Determinar si es un random walk o no
# Vamos a determinar si es un random walk o no. Recordar que es un proceso donde hay mismas posibilidades tanto de ir hacia arriba o hacia abajo por un número aleatorio.
# Step 1: Ver si existe una tendencia. En este caso, parece que puede haberlo ya que año a año ha ido incrementando.
## 1.a Vamos a descomponerlo en tendencia, temporalidad y residuos

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from statsmodels.tsa.seasonal import seasonal_decompose, STL

advanced_decomposition = STL(df['Precio'], period = 12).fit()

fig = make_subplots(rows=4, cols=1, subplot_titles=("Observed", "Trend", "Seasonal", "Residuals"))

fig.add_trace(
    go.Line(x = df.Fecha, y = advanced_decomposition.observed),
    row=1, col=1
)
fig.add_trace(
    go.Line(x = df.Fecha, y = advanced_decomposition.trend),
    row=2, col=1
)
fig.add_trace(
    go.Line(x = df.Fecha, y = advanced_decomposition.seasonal),
    row=3, col=1
)
fig.add_trace(
    go.Line(x = df.Fecha, y = advanced_decomposition.resid),
    row=4, col=1
)

# Efectivamente, vemos una tendencia en la segunda gráfica. Vamos a salir de dudas con test ADF para ver el ACF(Autocorrelation function):

from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf

ADF_result = adfuller(df.Precio)

print(f'ADF Statistic: {ADF_result[0]}')
print(f'p-value: {ADF_result[1]}')

plot_acf(df.Precio, lags=12) # Vemos como hay una relación linela en las muestras y por tanto, es no estacionario. Dentro del confidence interval se considera que es como tener 0

# Como el p valor es 0.79 y es mayor que 0.05, no podemos rechazar la null hyphotesis y por tanto es no estacionacionaria. Por ende, tennemos que diferenciar.

diff_gasolina = np.diff(df['Precio'], n = 1)
print(f'ADF Statistic: {diff_gasolina[0]}')
print(f'p-value: {diff_gasolina[1]}')
plot_acf(diff_gasolina, lags = 12) # Vemos como tenemos coeficientes significativos después de 0, esto q  uiere decir que es un random walk claramente

ADF_result = adfuller(diff_gasolina)
print(f'ADF Statistic: {ADF_result[0]}')
print(f'p-value: {ADF_result[1]}')


####### Probamos Moving Average


df_diff = pd.DataFrame({'diff_gasolina': diff_gasolina})

train = df_diff[:int(0.7*len(df_diff))]
test = df_diff[int(0.7*len(df_diff)):]


from statsmodels.tsa.statespace.sarimax import SARIMAX

def rolling_forecast(df: pd.DataFrame, train_len: int, horizon: int, window: int) -> list:
    
    total_len = train_len + horizon

    pred_MA = []
    
    for i in range(train_len, total_len, window):
        model = SARIMAX(df[:i], order=(0,0,1))
        res = model.fit(disp=False)
        predictions = res.get_prediction(0, i + window - 1)
        oos_pred = predictions.predicted_mean.iloc[-window:]
        pred_MA.extend(oos_pred)
        
    return res, pred_MA


pred_df = test.copy()
TRAIN_LEN = len(train)
HORIZON = len(test)
WINDOW = 1
    

res, pred_MA = rolling_forecast(df_diff, TRAIN_LEN, HORIZON, WINDOW)

pred_df['pred_MA'] = pred_MA



####----------------------###
import plotly.graph_objects as go

def draw_trace(data,legend_name,len_test=len(test)):
    trace = go.Scatter(
    x = df['Fecha'][-len_test:],
    y = data, name = legend_name)
    
    return trace   

trace1 =  go.Scatter(
    x = df['Fecha'][1:],
    y = df_diff['diff_gasolina'], name = '')

trace2 = draw_trace(pred_df['diff_gasolina'], 'Actual')


trace5 = draw_trace(pred_df['pred_MA'], 'MA')

traces = [trace1, trace2, trace5]
fig2 = go.Figure(data=traces)
fig2.show()


## New

df_ojo = df_diff.copy()
res.predict()

df_diff


from pandas.tseries.offsets import DateOffset

# Creamos dataframe futuro a Null
pred_date = df.copy()
pred_date = pred_date.set_index('Fecha')
pred_date=[pred_date.index[-1]+ DateOffset(months=x)for x in range(0,24)]
pred_date=pd.DataFrame(index=pred_date[1:],columns=df.columns)
pred_date


len(res.predict())


pred_MA
