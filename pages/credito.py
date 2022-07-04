# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 12:09:16 2022

@author: carlo
"""

import dash
from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import pandas as pd
from datetime import date
import numpy as np
import plotly.express as px
import pickle

df = pd.read_csv("data/data.csv")

register_page(__name__,path='/credito')


mensajes = ["Tu cliente es idóneo para continuar con la solicitud",
            "En este momento no es posible continuar con la slicitud",
            "De acuerdo a las características de tu cliente esta solicitud será consultada por un analista de crédito en AgriCapital"]

### load ML model ###########################################
with open('model/log_model.pickle', 'rb') as f:
    model = pickle.load(f)

layout=  dbc.Container(
    [
        dbc.Row([
                html.Div([
    html.H1(children='AgriCapital',
                style={
            'textAlign': 'center'}),
    html.H4(children='-Portal de solicitudes-',
                style={
            'textAlign': 'center'})
])
            ]),

        dbc.Row([
                html.H5(children='En este módulo podrás gestionar las solicitudes de crédito \
           para que tus clientes puedan acceder a los insumos y herramientas \
           necesarios para crecer.', style = {'marginBottom':'2.5em'}),
                ]),
                
                dbc.Row([
                ]),

                dbc.Row([
                ]),
       
        dbc.Row([
                html.H4(children='Formulario de solicitud',style={
            'textAlign': 'center'}),
                ]),

        dbc.Row([
                
               
                dbc.Col([
                        
                        html.P(children='1. ¿El cliente cuenta con vías de acceso que le permitan transportar sus productos?'),
                        dcc.Dropdown(
                                #df['viaacceso'].unique(),
                                ["Sí","No"],
                                'Seleccionar',
                                id='via_id',
                                style = {"width": '50%',
                                         'marginBottom':'2.5em'})
                        ]),
    
                    dbc.Col([
                        
                        html.P(children='2. ¿Cuál será el plazo del crédito solicitado?'),
                        dcc.Dropdown(
                                #df['plazo'].unique(),
                                [30,60,90,120,180,360,540,720],
                                id='plazo_id',
                                style = {"width": '50%',
                                         'marginBottom':'2.5em'})
                        ])
    
                
                ]),
    
    dbc.Row([
            
            dbc.Col([
                        
                        html.P(children='3. ¿Cuál es el monto solicitado?'),
                        dcc.Input(id='monto_id',type = "number",
                                style = {"width": '25%',
                                         'marginBottom':'2.5em'})
                        ])
            
            ]),
        
                dbc.Row([
                
                        dbc.Button('Implementar', id='submit-val', n_clicks=0, color="primary",
                                   style = {"width": '25%',
                                            'marginBottom':'2.5em'})
                        ]),
    
              dbc.Row([
                      html.Div(id='prediction_output',style={'marginUpper':'4.5em'})
              ]),
])

@callback(
        Output('prediction_output', 'children'),
        Input("submit-val", "n_clicks"),
        State("via_id", "value"),
        State("plazo_id", "value"),
        State("monto_id", "value")
        )
#
def update_output(n_clicks,via_val,plazo,monto):
    
    if plazo == None:
        plazo = 0
    
    if monto == None:
        monto = 0
        
    if via_val == "Sí":
        p = 0
    else:
        p = 1
    
    new = pd.DataFrame([[monto, plazo , float(p), float(0), float(0),
                     float(0), float(1), float(0), float(0),
                     float(0),float(0),float(1),float(0)]])
    prediction = model.predict(new)[0]
#
    if n_clicks == 0:
        return ""
    else:
        return f'{prediction}'


#@callback(
#    Output('output-container-date-picker-single', 'children'),
#    Input('my-date-picker-single', 'date'),
#    Input('nombre_id', 'value'),
#    Input('muni_id', 'value'))
#
#def update_output(date_value,name,muni):
#    return [date_value, name, muni]