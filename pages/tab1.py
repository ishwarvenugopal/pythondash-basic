from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output

from app import app

def tab1_contents():
    tab = [
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.H3(id='dropdown-value', style={'marginLeft':'2rem'}),
                                width=2
                            ),
                            dbc.Col(
                                dcc.Dropdown(
                                    id='dropdown-selection',
                                    options=[
                                        {'label': 'Dropdown item 1', 'value': 'Dropdown item 1'},
                                        {'label': 'Dropdown item 2', 'value': 'Dropdown item 2'},
                                    ],
                                    value='Nothing Selected',
                                ),
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

@app.callback(
   Output('dropdown-value', 'children'),
   Input('dropdown-selection', 'value'),
)
def update_values(value):
    return html.P('Selected value: {}'.format(value))
