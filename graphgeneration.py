from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app= Dash(__name__)

df= pd.read_csv("data/data on toddlers.csv")
df1=pd.read_csv("data/data on adults.csv")

fig= px.bar(df,
                x="Ethnicity"
                # , y="Ethnicity"
                ,color="Class/ASD Traits "
               , barmode="group"
                # ,size="Age_Mons"
                # ,  hover_name="Ethnicity"
                # ,log_x=True
                # ,size_max=60000
                )

fig1= px.bar(df1,
                x="ethnicity"
                # , y="Ethnicity"
                ,color="Class/ASD"
               , barmode="group"
             # , hover_data="Sex"
                # ,size="Age_Mons"
                # ,  hover_name="Ethnicity"
                # ,log_x=True
                # ,size_max=60000
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
    # Toddler Data in plotting
    html.Div(children=[html.H1(
                     children="Toddeler-Ethnictiy vs ASD Traits",
                     style={
                         'textAlign': 'center'
                     }),
    dcc.Graph(
        id='Ethnicity-vs-ASD-Traits',
        figure= fig
    )])
    ,
    # Adult data in plotting
    html.Div(children=[html.H1(
                     children="Adult-Ethnictiy vs ASD Traits",
                     style={
                         'textAlign': 'right'
                     }),
    dcc.Graph(
        id='Adult-Ethnicity-vs-ASD-Traits',
        figure= fig1
    )])
], style={'display': 'flex', 'flex-direction': 'row'})


if __name__ == '__main__':
    app.run_server(debug=True, port=8083)