from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output

def tab2_contents():
    tab = [
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.H3('Write code for Tab 2 components', style={'marginLeft':'2rem'}),
                                width=2
                            )
                        ],
                        style={
                            'align-contents':'center'
                        }
                    ),  
                ]
            ),
            style={
                'boxShadow': '0px 0px 0px 0px',
                'padding-top':'10px',
            }
        ),
    ] 

    return tab