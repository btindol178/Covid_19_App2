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
import dash_table



df = pd.read_csv("bar_chartbymonth2.csv",index_col=0, parse_dates=True)

app = dash.Dash()

app.layout = html.Div([
    html.Div([
        html.Pre(children="March Analysis",
                 style={"text-align": "center", "font-size": "100%", "color": "black"})
    ]),

    html.Div([
        html.Label(['March2020'], style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='drop1',
            options=[
                {'label': 'Feb', 'value':2 },
                {'label': 'Mar', 'value': 3},

            ],
            value='Mar',
            style={"width": "50%"}
        ),
    ]),
    html.Div([
        dcc.Graph(id='bar1')
    ])
])


@app.callback(Output(component_id='bar1', component_property='figure'),
    [Input(component_id='drop1', component_property='value')])
def update_graph(drop1):
    dff1 = df[df['month'] == drop1]


    barchart1 = px.bar(
        data_frame=dff1,
        x='TranType',
        y='Count',
        title='Output'
    )
    
    return barchart1


if __name__ == '__main__':
    app.run_server