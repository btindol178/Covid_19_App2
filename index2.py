# ADD A DATEPICKERRANGE COMPONENT FOR START & END DATE INPUT
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web # requires v0.6.0 or later
from datetime import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


df = pd.read_csv('data/covid_df2.csv',index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['date'])

external_stylesheets = [dbc.themes.BOOTSTRAP]


app = dash.Dash()
app.config.suppress_callback_exceptions = True

def get_options(list_states):
    dict_list = []
    for i in list_states:
        dict_list.append({'label': i, 'value': i})

    return dict_list

app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(id='stateselector', options=get_options(df['state'].unique()),
                                                      multi=True, value=[df['state'].sort_values()[0]],
                                                      style={'backgroundColor': '#243745'},
                                                      className='stateselector'
                                                      )),
                dbc.Col(html.Div("two of one columns")),
                dbc.Col(html.Div("three of one columns")),
            ],
            align="start",
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("One of Two columns")),
                dbc.Col(html.Div("Two of Two columns")),
                dbc.Col(html.Div("Three of Two columns")),
            ],
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("Two of three columns")),
                dbc.Col(html.Div("Three of three columns")),
            ],
            align="end",
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("One of Four columns"), align="start"),
                dbc.Col(html.Div("One of Four columns"), align="center"),
                dbc.Col(html.Div("One of Four columns"), align="end"),
            ]
        ),
    ]
)


if __name__ == '__main__':
     app.run_server(debug=True)
