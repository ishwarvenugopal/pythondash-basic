from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from app import app

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