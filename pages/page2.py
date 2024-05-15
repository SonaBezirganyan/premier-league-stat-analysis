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
                   path="/barplot",
                   name="Top Player Statistics",
                   title="Top Player Statistics"
                   )


df  = data_preprocessing.read_and_preprocess_data()


features = ['Appearances', 'Goals', 'Goals per match', 'Wins', 'Wins per match', 'Losses', 'Losses per match',
'Tackles', 'Tackles per match', 'Saves', 'Saves per match', 'Clean sheets', 'Clean sheets per match']


layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(id="column_selector2", options=[{"label":x, "value":x} for x in features], multi=False, value=features[0]),
                dcc.Graph(id="column_selector_graph2", figure={})])
        ])

])


@callback(
    Output('column_selector_graph2', 'figure'),
    Input('column_selector2', 'value')
)
def update_graph(feature):
    df_sorted = df.sort_values(by=feature, ascending=False)
    fig = px.bar(df_sorted.head(10), x='Name', y=feature, title=f"Top players by {feature}", text=feature)
    fig.update_layout(xaxis_tickangle=25)
    return fig