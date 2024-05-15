import pandas as pd

def read_and_preprocess_data():
    df = pd.read_csv("pl_player_statistics.csv")
    relevant_columns = ['Name', 'Club', 'Position', 'Nationality', 'Age', 'Appearances', 'Wins', 'Losses', 'Goals', 'Goals per match', 
        'Shots', 'Shots on target', 'Shooting accuracy %', 'Big chances missed', 'Clean sheets', 'Goals conceded', 'Tackles',
        'Tackle success %', 'Errors leading to goal', 'Assists', 'Passes', 'Passes per match', 'Big chances created', 'Saves', 
        'Penalties saved', 'Yellow cards', 'Red cards']
    df = df.loc[:, relevant_columns]
    df['Shooting accuracy %'] = df['Shooting accuracy %'].str.rstrip('%').astype(float)
    df['Shooting accuracy %'].head()
    df['Tackle success %'] = df['Tackle success %'].str.rstrip('%').astype(float)
    df['Tackle success %'].head()
    df = df.dropna(subset=['Age', 'Nationality'])
    df = df[df['Appearances'] != 0]
    df['Goals per match'] = df['Goals'] / df['Appearances']
    df['Wins per match'] = df['Wins'] / df['Appearances']
    df['Losses per match'] = df['Losses'] / df['Appearances']
    df['Tackles per match'] = df['Tackles'] / df['Appearances']
    df['Saves per match'] = df['Saves'] / df['Appearances']
    df['Clean sheets per match'] = df['Clean sheets'] / df['Appearances']
    df['Assists per match'] = df['Assists'] / df['Appearances']

    return df