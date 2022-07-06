# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 21:14:26 2022

@author: carlo
"""

#libraries
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc

#from callbacks import register_callbacks


#request_path_prefix = None

#only for workspace in DS4A
#workspace_user = os.getenv('JUPYTERHUB_USER')  # Get DS4A Workspace user name
#if workspace_user:
#    request_path_prefix = '/user/' + workspace_user + '/proxy/8050/'

    
# Dash instance declaration
app = dash.Dash(__name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.FLATLY],)



#Top menu, items get from all pages registered with plugin.pages
navbar = dbc.NavbarSimple([

    dbc.NavItem(dbc.NavLink("AgriCapital")),
#    dbc.DropdownMenu(
#        [
#
#            dbc.DropdownMenuItem(page["name"], href=request_path_prefix+page["path"])
#            for page in dash.page_registry.values()
#            if page["module"] != "pages.not_found_404"
#        ],
#        nav=True,
#        label="Data Science",
#    ),
    dbc.NavItem(dbc.NavLink("Agro-loans", href="/credito")),
    ],
    brand="DS4A Project - Team 184",
    color="primary",
    dark=True,
    className="mb-2",
)

#Main layout
app.layout = dbc.Container(
    [
        navbar,
        dl.plugins.page_container,
    ],
    className="dbc",
    fluid=True,
)

# Call to external function to register all callbacks
#register_callbacks(app)


# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run_server(debug=True)