#import required libraries
import plotly
import plotly.graph_objects as go
import pandas as pd

# declare file, this can changed to sys.agv
excel_file = 'BTC_USD_2013-10-01_2020-10-29-CoinDesk.csv'

# create the database
df = pd.read_csv(excel_file)

#create a new database
new_df = df.loc[:, "Date":"Closing Price (USD)"]

#create the simple moving average

simple_moving_average = new_df.rolling(window=7, on='Date').mean() # .min() #max() #.sum()



# declare data visualistaion

data = [go.Scatter( x=simple_moving_average['Date'], y=simple_moving_average['Closing Price (USD)'])]

#plot figure

fig = go.Figure(data)

#add detail

fig.update_layout(
    title= 'Bitcoin Closig Price',
    xaxis_title= 'Date',
    yaxis_title= 'Closing Price'
)
#show figure

fig.show()
