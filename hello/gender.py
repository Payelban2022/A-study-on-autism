
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server=app.server

class GenderGraph:
    def getgenderGraph(self):
        print("I am payel")
        df = pd.read_csv("https://payelpassionproject.s3.amazonaws.com/dataonautism/inputdata/data+on+toddlers.csv")
        df1 = pd.read_csv("https://payelpassionproject.s3.amazonaws.com/dataonautism/inputdata/data+on+adults.csv")

        fig = px.bar(df,
                     x="Sex",
                     # color="ethnicity",
                     barmode="group")



        fig1 = px.bar(df1,
                      x = "gender",
                      color="age_desc",
                      barmode="group")

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

        app.layout = html.Div([
            # Ethnicity Data in plotting
            html.Div(children=[html.H1(
                children="Gender vs ASD Traits(Toddlers)",
                style={
                    'textAlign': 'center'
                }),
                dcc.Graph(
                    id='Gender on ASD',
                    figure=fig
                )])
            ,
            # Gender Data in plotting
            html.Div(children=[html.H1(
                children="Gender vs ASD Traits(Adults)",
                style={
                    'textAlign': 'center'
                }),
                dcc.Graph(
                    id='sex on ASD',
                    figure=fig1
                )])

        ], style={'display': 'flex', 'flex-direction': 'row'})

if __name__ == '__main__':
    GenderGraph.getgenderGraph('')
    app.run_server(debug=True, port=8087)
