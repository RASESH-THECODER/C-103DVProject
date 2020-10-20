import pandas as pd 
import plotly.express as px 

df=pd.read_csv("data - data.csv")

fig=px.line(df,x='country',y='cases')
fig.show()