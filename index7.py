# ADD A DATEPICKERRANGE COMPONENT FOR START & END DATE INPUT
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web # requires v0.6.0 or later
from datetime import datetime
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


df = pd.read_csv('covid_df2.csv',index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['date'])

external_stylesheets = [dbc.themes.BOOTSTRAP]


app = dash.Dash()
app.config.suppress_callback_exceptions = True

def get_options(list_states):
    dict_list = []
    for i in list_states:
        dict_list.append({'label': i, 'value': i})

    return dict_list

app.layout = html.Div(className='row', children=[
    html.H1("Covid Dashboard",style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div(children=[
        dcc.Dropdown(id='stateselector', options=get_options(df['state'].unique()),
                                                      multi=True, value=[df['state'].sort_values()[0]],
                                                      style=dict(width='50%', alignitmes = "right", justifycontent = "right", display = 'inline-block'),
                                                      className='stateselector'
                                                      ),
        dcc.Dropdown(id='stateselector1', options=get_options(df['state'].unique()),
                                                      multi=True, value=[df['state'].sort_values()[0]],
                                                      style=dict(width='50%', alignitmes = "right", justifycontent = "right", display = 'inline-block'),
                                                      className='stateselector1'
                                                      )
    ]),
            
    html.Div(children=[
        dcc.Graph(id='timeseries', config={'displayModeBar': False}, animate=True,style={'display': 'inline-block'}),
        dcc.Graph(id='timeseries1', config={'displayModeBar': False}, animate=True,style={'display': 'inline-block'})
        
    ])
])


# Callback for timeseries price
@app.callback(Output('timeseries', 'figure'),
              [Input('stateselector', 'value')])
def update_graph(selected_dropdown_value):
    trace1 = []
    df_sub = df
    for state in selected_dropdown_value:
        trace1.append(go.Scatter(x=df_sub[df_sub['state'] == state].index,
                                 y=df_sub[df_sub['state'] == state]['retail'],
                                 mode='lines',
                                 opacity=0.7,
                                 name=state,
                                 textposition='bottom center'))
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'StateMobility', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
              ),

              }

    return figure

# Callback for timeseries price
@app.callback(Output('timeseries1', 'figure'),
              [Input('stateselector1', 'value')])
def update_graph(selected_dropdown_value):
    trace1 = []
    df_sub = df
    for state in selected_dropdown_value:
        trace1.append(go.Scatter(x=df_sub[df_sub['state'] == state].index,
                                 y=df_sub[df_sub['state'] == state]['retail'],
                                 mode='lines',
                                 opacity=0.7,
                                 name=state,
                                 textposition='bottom center'))
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                  template='plotly_dark',
                  paper_bgcolor='rgba(0, 0, 0, 0)',
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'StateMobility', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
              ),

              }

    return figure

if __name__ == '__main__':
     app.run_server(debug=True)

