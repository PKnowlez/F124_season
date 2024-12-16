import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image

def Calculations():
    # Read in excel sheet
    df = pd.read_excel('F124_season.xlsx', sheet_name='PythonReadyData')

    race_points = ['SuzukaPoints','SilverstonePoints','AustraliaPoints', 
                    'SpaPoints','SpainPoints','ChinaSprintPoints','ChinaPoints', 
                    'BakuPoints','CanadaPoints','MonzaPoints','Abu DhabiPoints', 
                    'AustriaSprintPoints','AustriaPoints','COTASprintPoints','COTAPoints']
    race_place = ['SuzukaPlace','SilverstonePlace','AustraliaPlace', 
                    'SpaPlace','SpainPlace','ChinaSprintPlace','ChinaPlace', 
                    'BakuPlace','CanadaPlace','MonzaPlace','Abu DhabiPlace', 
                    'AustriaSprintPlace','AustriaPlace','COTASprintPlace','COTAPlace']
    fastest_lap = ['SuzukaFastestLap','SilverstoneFastestLap','AustraliaFastestLap', 
                    'SpaFastestLap','SpainFastestLap','ChinaSprintFastestLap','ChinaFastestLap', 
                    'BakuFastestLap','CanadaFastestLap','MonzaFastestLap','Abu DhabiFastestLap', 
                    'AustriaSprintFastestLap','AustriaFastestLap','COTASprintFastestLap','COTAFastestLap']
    qualifying = ['SuzukaQualifying','SilverstoneQualifying','AustraliaQualifying', 
                    'SpaQualifying','SpainQualifying','ChinaSprintQualifying','ChinaQualifying', 
                    'BakuQualifying','CanadaQualifying','MonzaQualifying','Abu DhabiQualifying', 
                    'AustriaSprintQualifying','AustriaQualifying','COTASprintQualifying','COTAQualifying']
    races = ['Suzuka','Silverstone','Australia', 
                    'Spa','Spain','China (S)','China', 
                    'Baku','Canada','Monza','Abu Dhabi', 
                    'Austria (S)','Austria','COTA (S)','COTA']

    drivers = df['Driver']
    teams = df['Team']
    starting = df['Starting']

    df['Total'] = 0
    for i in range(len(race_points)):
        df['Total'] = df['Total'] + df[race_points[i]]

    team_race_totals = pd.DataFrame([]) 
    for i in range(len(race_points)):
        if i == 0:
            team_race_totals[race_points[i]] = df.groupby('Team')[race_points[i]].sum()
        else:
            team_race_totals[race_points[i]] = df.groupby('Team')[race_points[i]].sum() \
                                                    + team_race_totals[race_points[i-1]]

    driver_race_totals = pd.DataFrame([])
    for i in range(len(race_points)):
        if i == 0:
            driver_race_totals[race_points[i]] = df.groupby('Driver')[race_points[i]].sum()
        else:
            driver_race_totals[race_points[i]] = df.groupby('Driver')[race_points[i]].sum() \
                                                    + driver_race_totals[race_points[i-1]]

    total = df['Total']
    team_totals = df.groupby('Team')['Total'].sum()
    team_totals_sorted = team_totals.sort_values(ascending=False)

    # Define team colors
    team_colors = {
        'Alpine': 'hotpink', 
        'Aston Martin': 'teal',
        'Ferrari': 'red',
        'McLaren': 'darkorange',
        'Red Bull': 'darkblue',
        'VCARB': 'blue'
    }

    # Driver colors
    color_list = ['darkorange','orange','blue','skyblue','red','#ff6060','pink','hotpink','darkblue','#8888c9','#84c1c1','teal']
    driver_colors = {}  # Initialize an empty dictionary
    for i, driver in enumerate(drivers.unique()):
        driver_colors[driver] = color_list[i % len(color_list)]

    for i in range(len(race_place)):
        if df.loc[0,race_points[i]] == 0:
            index = i
            index_x = index-0.5
            break
        else:
            x = 0

    # --- Team Plot ---

    # Add a new column of zeros at the beginning
    team_race_totals.insert(0, 'Start', 0)  
    team_race_totals = team_race_totals.T

    races.insert(0, 'Start') 

    # Create Plotly figure
    fig1 = go.Figure()

    for team in team_race_totals.columns:
        fig1.add_trace(go.Scatter(x=races,
                                y=team_race_totals[team], 
                                mode='lines+markers',
                                name=team, 
                                line=dict(color=team_colors.get(team))))

    fig1.update_layout(
        xaxis_range=[0,index],
        xaxis_title="Race",
        yaxis_title="Total Points",
        title="Constructor's Championship",
        hovermode="x unified"  # Enhanced hover mode for better readability
    )

    # --- Driver Plot ---

    # Add a new column of zeros at the beginning
    driver_race_totals.insert(0, 'Start', 0)  
    driver_race_totals = driver_race_totals.T 

    # Create Plotly figure
    fig2 = go.Figure()

    for driver in driver_race_totals.columns:
        fig2.add_trace(go.Scatter(x=races,
                                y=driver_race_totals[driver], 
                                mode='lines+markers',
                                name=driver,
                                line=dict(color=driver_colors.get(driver))))

    fig2.update_layout(
        xaxis_range=[0,index],
        xaxis_title="Race",
        yaxis_title="Total Points",
        title="Driver's Championship",
        hovermode="x unified"  # Enhanced hover mode for better readability
    )

    return team_race_totals,driver_race_totals,df,races,team_colors,fig1,fig2,race_place,race_points,index_x