
import dash
import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div("One of one columns")),
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
