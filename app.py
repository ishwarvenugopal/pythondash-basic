import dash
import dash_bootstrap_components as dbc
import dash_auth

VALID_USERNAME_PASSWORD_PAIRS = {
    'test': 'test'
}

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.GRID]) 

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)