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
                   path="/barplot_combined",
                   name="Player Statistics by Positions",
                   title="Player Statistics by Positions"
                   )


df  = data_preprocessing.read_and_preprocess_data()



def update_graph():
    df_sorted_saves = df.sort_values(by='Saves', ascending=False).head(10)
    df_sorted_saves_per_match = df.sort_values(by='Saves per match', ascending=False).head(10)
    df_sorted_clean_sheets = df.sort_values(by='Clean sheets', ascending=False).head(10)
    df_sorted_clean_sheets_per_match = df.sort_values(by='Clean sheets per match', ascending=False).head(10)

    fig = make_subplots(rows=2, cols=2, subplot_titles=("Number of Saves", "Saves per Match", "Clean Sheets", "Clean Sheets per Match"), vertical_spacing=0.2)

    fig.add_trace(go.Bar(x=df_sorted_saves['Name'], y=df_sorted_saves['Saves'], name='Number of Saves'), row=1, col=1)
    fig.add_trace(go.Bar(x=df_sorted_saves_per_match['Name'], y=df_sorted_saves_per_match['Saves per match'], name='Saves per Match'), row=1, col=2)
    fig.add_trace(go.Bar(x=df_sorted_clean_sheets['Name'], y=df_sorted_clean_sheets['Clean sheets'], name='Clean Sheets'), row=2, col=1)
    fig.add_trace(go.Bar(x=df_sorted_clean_sheets_per_match['Name'], y=df_sorted_clean_sheets_per_match['Clean sheets per match'], name='Clean Sheets per Match'), row=2, col=2)

    fig.update_layout(height=1000, width=1300, title_text="Top 10 Goalkeepers Statistics")
    return fig


features = ['Goalkeeping', 'Attacking', 'Defending']


layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(id="column_selector3", options=[{"label":x, "value":x} for x in features], multi=False, value=features[0]),
                dcc.Graph(id="column_selector_graph3", figure={})])
        ])

])


@callback(
    Output('column_selector_graph3', 'figure'),
    Input('column_selector3', 'value')
)
def update_graph(feature):
    if feature == 'Goalkeeping':
        df_sorted_saves = df.sort_values(by='Saves', ascending=False).head(10)
        df_sorted_saves_per_match = df.sort_values(by='Saves per match', ascending=False).head(10)
        df_goalkeepers = df[df['Position'] == 'Goalkeeper']
        df_sorted_clean_sheets = df_goalkeepers.sort_values(by='Clean sheets', ascending=False).head(10)
        df_sorted_clean_sheets_per_match = df_goalkeepers.sort_values(by='Clean sheets per match', ascending=False).head(10)

        fig = make_subplots(rows=2, cols=2, subplot_titles=("Number of Saves", "Saves per Match", "Clean Sheets", "Clean Sheets per Match"), vertical_spacing=0.2)

        fig.add_trace(go.Bar(x=df_sorted_saves['Name'], y=df_sorted_saves['Saves'], name='Number of Saves'), row=1, col=1)
        fig.add_trace(go.Bar(x=df_sorted_saves_per_match['Name'], y=df_sorted_saves_per_match['Saves per match'], name='Saves per Match'), row=1, col=2)
        fig.add_trace(go.Bar(x=df_sorted_clean_sheets['Name'], y=df_sorted_clean_sheets['Clean sheets'], name='Clean Sheets'), row=2, col=1)
        fig.add_trace(go.Bar(x=df_sorted_clean_sheets_per_match['Name'], y=df_sorted_clean_sheets_per_match['Clean sheets per match'], name='Clean Sheets per Match'), row=2, col=2)

        fig.update_layout(height=1000, width=1300, title_text="Top 10 Goalkeeping Statistics")
        return fig
    elif feature == 'Attacking':
        df_sorted_goals = df.sort_values(by='Goals', ascending=False).head(10)
        df_sorted_goals_per_match = df.sort_values(by='Goals per match', ascending=False).head(10)
        df_sorted_shots = df.sort_values(by='Assists', ascending=False).head(10)
        df_sorted_shots_per_match = df.sort_values(by='Assists per match', ascending=False).head(10)

        fig = make_subplots(rows=2, cols=2, subplot_titles=("Number of Goals", "Goals per Match", "Assists", "Assists per Match"), vertical_spacing=0.2)

        fig.add_trace(go.Bar(x=df_sorted_goals['Name'], y=df_sorted_goals['Goals'], name='Number of Goals'), row=1, col=1)
        fig.add_trace(go.Bar(x=df_sorted_goals_per_match['Name'], y=df_sorted_goals_per_match['Goals per match'], name='Goals per Match'), row=1, col=2)
        fig.add_trace(go.Bar(x=df_sorted_shots['Name'], y=df_sorted_shots['Assists'], name='Assists'), row=2, col=1)
        fig.add_trace(go.Bar(x=df_sorted_shots_per_match['Name'], y=df_sorted_shots_per_match['Assists per match'], name='Assists per Match'), row=2, col=2)

        fig.update_layout(height=1000, width=1300, title_text="Top 10 Attacking Statistics")
        return fig
    else:
        df_sorted_tackles = df.sort_values(by='Tackles', ascending=False).head(10)
        df_sorted_tackle_success = df.sort_values(by='Tackle success %', ascending=False).head(10)
        df_non_goalkeepers = df[df['Position'] != 'Goalkeeper']
        df_sorted_clean_sheets = df_non_goalkeepers.sort_values(by='Clean sheets', ascending=False).head(10)
        df_sorted_clean_sheets_per_match = df_non_goalkeepers.sort_values(by='Clean sheets per match', ascending=False).head(10)

        fig = make_subplots(rows=2, cols=2, subplot_titles=("Number of Tackles", "Tackle success %", "Clean Sheets", "Clean Sheets per Match"), vertical_spacing=0.2)

        fig.add_trace(go.Bar(x=df_sorted_tackles['Name'], y=df_sorted_tackles['Tackles'], name='Number of Tackles'), row=1, col=1)
        fig.add_trace(go.Bar(x=df_sorted_tackle_success['Name'], y=df_sorted_tackle_success['Tackle success %'], name='Tackle success %'), row=1, col=2)
        fig.add_trace(go.Bar(x=df_sorted_clean_sheets['Name'], y=df_sorted_clean_sheets['Clean sheets'], name='Clean Sheets'), row=2, col=1)
        fig.add_trace(go.Bar(x=df_sorted_clean_sheets_per_match['Name'], y=df_sorted_clean_sheets_per_match['Clean sheets per match'], name='Clean Sheets per Match'), row=2, col=2)

        fig.update_layout(height=1000, width=1300, title_text="Top 10 Defending Statistics")
        return fig



