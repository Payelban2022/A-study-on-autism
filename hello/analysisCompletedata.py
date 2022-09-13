from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app= Dash(__name__)

class CompleteAnalysis:
    def getCompleteAnalysis(self):
        df = pd.read_csv("Complete analysis on ASD.csv")

        fig = px.bar(df,
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

            ),

        app.layout= html.Div([
            html.Div(children=[html.H1(
                children="Analysis on Age and ethnicity vs ASD Traits",
                style={
                    'textAlign': 'center'
                }),
                dcc.Graph(
                    id='Gender,ethnicity-vs-Traits',
                    figure=fig)]),



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
    CompleteAnalysis.getCompleteAnalysis('')
    app.run_server(debug=True, port=8084)