# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 12:09:16 2022

@author: carlo
"""

import dash
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

register_page(__name__,path='/')

import pandas as pd
import plotly.express as px
import matplotlib as plt

df = pd.read_csv("data\data.csv")
df['Fecha Solicitud'] = pd.to_datetime(df['Fecha Solicitud']).dt.date

df1 = pd.DataFrame({'count': df.groupby(['Fecha Solicitud','productosolicitado'])['Fecha Solicitud'].count()}).reset_index()

df2 = pd.DataFrame({'count': df.groupby(['productosolicitado'])['MoraMáxima(SI/NO)'].value_counts()}).reset_index()
df2 = df2.replace({'MoraMáxima(SI/NO)':{1:"En mora",0:"Al día"}})

layout=  dbc.Container(
    [
        dbc.Row([
                html.Div([
    html.H1(children='AgriCapital',
                style={
            'textAlign': 'center'}),
    html.H6(children='-Operaciones financieras-',
                style={
            'textAlign': 'center'}),
    html.P(children='Bienvenido Aliado Agromaquinas S.A!'),
   ])
            ]),

        dbc.Row([
                dcc.Dropdown(
                df1['productosolicitado'].unique(),
                'Credi+',
                id='producto_cat',
                style = {"width": '50%'})
                ]),
                        
        dbc.Row([
                
                dbc.Col([
                        dcc.Graph(id='graph_1')
                        ]),
                
                dbc.Col([dcc.Graph(
        id='graph_2')]),
        
        ]),

        dbc.Row([
                html.P(children='A continuación te mostraremos cómo lucen algunas  \
           características de un cliente con un buen perfil crediticio')
                ]),     


        dbc.Row([
                
                dbc.Col([
                        dcc.Graph(id='graph_3')
                        ]),
                
                dbc.Col([
                        dcc.Graph(id='graph_4')
                ]),
        
        ]),    

]
)
                
@callback(
    Output("graph_1", "figure"),
    Input("producto_cat", "value"))

def display_line(producto):
    df_line = df1.loc[df['productosolicitado']==producto]
    figa = px.line(df_line, x='Fecha Solicitud', y='count', title = "Evolución en el número de créditos",
                   labels = {"Fecha Solicitud": "Fecha",
                             'count': "Número de créditos"})
    figa.update_traces(line_color="#67001f")
    return figa

@callback(
    Output("graph_2", "figure"),
    Input("producto_cat", "value"))

def display_line(producto):
    df_pie = df2.loc[df2['productosolicitado']==producto]
    figb = px.pie(df_pie,values = 'count', names= 'MoraMáxima(SI/NO)', title = 'Estado de los clientes',
                  labels = {'count':'Número',
                            'MoraMáxima(SI/NO)':'Estado Cartera'}, hole = .2, color_discrete_sequence=px.colors.sequential.RdBu)

    return figb

@callback(
    Output("graph_3", "figure"),
    Input("producto_cat", "value"))

def display_line(producto):
    df_hist1 = df.loc[df['productosolicitado']==producto]
    df_hist1 = df_hist1.replace({'MoraMáxima(SI/NO)':{1:"En mora",0:"Al día"}})
    figc = px.histogram(df_hist1,x = 'montosolicitado', color = 'MoraMáxima(SI/NO)', 
                        title = 'Monto solicitado', barmode='group',
                        labels = {"montosolicitado":"Monto",
                                  "MoraMáxima(SI/NO)":"Estado cartera"})

    return figc

@callback(
    Output("graph_4", "figure"),
    Input("producto_cat", "value"))

def display_line(producto):
    df_hist2 = df.loc[df['productosolicitado']==producto]
    df_hist2 = df_hist2.replace({'MoraMáxima(SI/NO)':{1:"En mora",0:"Al día"}})
    figd = px.histogram(df_hist2,x = 'plazo', color = 'MoraMáxima(SI/NO)', 
                        title = 'Plazo', barmode='group',
                        labels = {"MoraMáxima(SI/NO)":"Estado cartera",
                                  "plazo":"Plazo"})

    return figd