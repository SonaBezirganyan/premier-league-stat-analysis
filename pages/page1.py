import dash
from dash import dcc, html, callback
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web
import datetime
import plotly.graph_objects as go
import plotly.express as px

import data_preprocessing


dash.register_page(__name__,
                   path="/histogram",
                   name="Distribution of Numeric Columns",
                   title="Distribution of Numeric Columns"
                   )


df  = data_preprocessing.read_and_preprocess_data()


numeric_columns = ['Age', 'Appearances', 'Wins', 'Losses', 'Shots', 'Clean sheets', 
                    'Goals conceded', 'Saves', 'Penalties saved', 'Yellow cards', 'Red cards']


layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(id="column_selector", options=[{"label":x, "value":x} for x in numeric_columns], multi=False, value=numeric_columns[0]),
                dcc.Graph(id="column_selector_graph", figure={})])
        ])

])


@callback(
    Output('column_selector_graph', 'figure'),
    Input('column_selector', 'value')
)
def update_graph(column):
    return px.histogram(df, x=column)