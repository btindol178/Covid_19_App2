#######
# This is a stacked bar chart showing three traces
# (gold, silver and bronze medals won) for each country
# that competed in the 2018 Winter Olympics.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('barplot2.csv',index_col=0, parse_dates=True)

trace1 = go.Bar(
    x=df['state'],  # NOC stands for National Olympic Committee
    y=df['cases'],
    name = 'cases',
    marker=dict(color='#FFD700') # set the marker color to gold
)


data = [trace1]
layout = go.Layout(
    title='Top 10 States for Cumulative Covid Confirmed Cases ',
    barmode='stack'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar3.html')
