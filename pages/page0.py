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


dash.register_page(__name__,
                   path="/",
                   name="Home",
                   title="PL Stats Analysis",
                   )


layout = dbc.Container([
    dbc.Row(
        [
            dbc.Col([html.Img(src ='../assets/home_page_img.jpg',
                              style={"height":"80%", "width":"80%"}           
            )])
        ]
    )
])