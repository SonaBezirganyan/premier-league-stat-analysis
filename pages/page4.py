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
                   path="/boxplot",
                   name="Age Distribution",
                   title="Age Distribution"
                   )


df  = data_preprocessing.read_and_preprocess_data()


features = ['Club', 'Position']


layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(id="column_selector4", options=[{"label":x, "value":x} for x in features], multi=False, value=features[0]),
                dcc.Graph(id="column_selector_graph4", figure={})])
        ])

])


@callback(
    Output('column_selector_graph4', 'figure'),
    Input('column_selector4', 'value')
)
def update_graph(feature):
    if feature == 'Position':
        fig = go.Figure(data=go.Box(
            x=df['Position'],
            y=df['Age'],
            boxpoints='all',
            jitter=0.3,
            pointpos=-1.8,
            marker=dict(
                color='rgb(7,40,89)'
            ),
            line=dict(
                color='rgb(7,40,89)'
            ),
            fillcolor='rgba(0,0,0,0.1)',
            opacity=0.7
        ))

        fig.update_layout(
            title='Age Distribution by Position',
            xaxis_title='Position',
            yaxis_title='Age'
        )
        return fig
    else:
        fig = go.Figure(data=go.Box(
            x=df['Club'],
            y=df['Age'],
            boxpoints='all',
            jitter=0.3,
            pointpos=-1.8,
            marker=dict(
                color='rgb(7,40,89)'
            ),
            line=dict(
                color='rgb(7,40,89)'
            ),
            fillcolor='rgba(0,0,0,0.1)',
            opacity=0.7
        ))

        fig.update_layout(
            title='Age Distribution by Club',
            xaxis_title='Club',
            yaxis_title='Age'
        )
        return fig



