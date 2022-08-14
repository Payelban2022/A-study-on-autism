from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app= Dash(__name__)

df= pd.read_csv("Complete analysis on ASD.csv")

fig= px.bar(df,
                x="age-group"
                # , y="Ethnicity"
                ,color="Ethnicity"
               , barmode="group"
                )

fig1= px.bar(df,
                x="Gender"
                # , y="Ethnicity"
                ,color="age-group"
               , barmode="group"
                )

fig.update_layout(
    plot_bgcolor='#111111',
    paper_bgcolor='#111111',
    font_color='#7FDBFF'

)
fig1.update_layout(
    plot_bgcolor='#111111',
    paper_bgcolor='#111111',
    font_color='#7FDBFF'

)

app.layout= html.Div([
    # Ethnicity Data in plotting
    html.Div(children=[html.H1(
                     children="Analysis on Ethnictiy vs ASD Traits on All Ages",
                     style={
                         'textAlign': 'center'
                     }),
    dcc.Graph(
        id='Ethnicity-vs-Traits',
        figure= fig
    )])
    ,
    # Gender Data in plotting
    html.Div(children=[html.H1(
        children="Analysis on Age vs ASD Traits",
        style={
            'textAlign': 'center'
        }),
        dcc.Graph(
            id='Gender-vs-Traits',
            figure=fig1
        )])

], style={'display': 'flex', 'flex-direction': 'row'})


if __name__ == '__main__':
    app.run_server(debug=True, port=8084)