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
from plotly.subplots import make_subplots

import data_preprocessing


dash.register_page(__name__,
                   path="/stacked_barplot",
                   name="Club Statistics",
                   title="Club Statistics"
                   )


df  = data_preprocessing.read_and_preprocess_data()



def update_graph():
    trace_goals = go.Bar(
        x=df['Club'],
        y=df['Goals'],
        name='Goals'
    )

    trace_assists = go.Bar(
        x=df['Club'],
        y=df['Yellow cards'],
        name='Yellow cards'
    )

    trace_wins = go.Bar(
        x=df['Club'],
        y=df['Wins'],
        name='Wins'
    )

    data = [trace_goals, trace_assists, trace_wins]

    layout = go.Layout(
        barmode='stack',
        title='Distribution of Goals, Yellow cards, and Wins for Each Club',
        xaxis=dict(title='Club'),
        yaxis=dict(title='Count')
    )

    fig = go.Figure(data=data, layout=layout)
    return fig



layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Graph(id="column_selector_graph5", figure=update_graph())
            ])
        ])

])