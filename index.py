from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from app import app
from pages import tab1, tab2

def serve_layout():
    return dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                            [
                                dbc.CardImg(src="/static/images/dummy_logo.jpg", style={'height': '3rem', 'width': 'auto', 'padding': '5px'}),
                            ],
                            style={
                                'boxShadow': '0px 0px 0px 0px',
                            }
                        ),
                )
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Tabs(
                                [
                                    dcc.Tab(tab1.tab1_contents(), value = 'tab1', label='Tab 1'),
                                    dcc.Tab(tab2.tab2_contents(), value='tab2', label='Tab 2'),
                                ],
                                value = 'tab1',
                                id='tabs-master',
                                style = {
                                    'padding-top': '5px'
                                }
                            )
                        ]
                    )
                ]
            )
        ],
        fluid = True,
        style = {
            'width':'auto'
        }
    )

app.layout = serve_layout

if __name__ == '__main__': 
	app.run_server(debug=True, host='0.0.0.0', port=8051)