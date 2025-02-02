import pandas as pd
import plotly.graph_objects as go
import numpy as np

df = pd.read_csv(r'Datasets\electricity_data.csv')
df = df[1110:]
df.reset_index(drop=True, inplace=True)
df.index = pd.to_datetime(df['Date'])

df2 = pd.read_csv(r'Datasets\electrical_appliance_consumption.csv')
df2 = df2[df2['year'] == 2023]
df2.reset_index(drop=True, inplace=True)

df3 = pd.read_csv(r'Datasets\electrical_forecast.csv')

df4 = pd.read_csv(r'Datasets\electricity_appliance_wise_data.csv')
df4['Date'] = pd.to_datetime(df4['Date'])
df4 = df4[df4['Date'].dt.year == 2023]
df4.reset_index(drop=True, inplace=True)

import dash
from dash import html
from dash.dependencies import Input, Output

from dash import dcc
import plotly.express as px

app = dash.Dash(__name__)
app.title = 'Green Energy Optimiser'

party_data = []
for x in ['Monthwise Energy Consumption', 'Appliance-wise Consumption', 'Electricity Consumption Forecast']:
        party_data.append({'label': x, 'value': x})

# Define the app

app.layout = html.Div(children=[
    html.Div(className='row', children=[
        html.Div(className='twelve column div-for-charts bg-grey', children=[
            dcc.Graph(id='timeseries', config={'displayModeBar': False}),
            # Add the dropdown menu below the graph
            html.Div(className='div-for-dropdown', children=[
                dcc.Dropdown(id='stockselector',
                             options=party_data,
                             value=['Time-Series Plot'],
                             style={'backgroundColor': '#1E1E1E'},
                             placeholder="")
            ])
        ]),
    ]),
])

@app.callback(Output('timeseries', 'figure'),
              [Input('stockselector', 'value')])
def update_timeseries(selected_dropdown_value):
    ''' Draw traces of the feature 'value' based one the currently selected stocks '''
    if (selected_dropdown_value == 'Electricity Consumption Forecast'):
        df_sub = df3
        df_anoms = df_sub[df_sub['MAE']>= 15]
        df_anoms.reset_index(drop=True, inplace=True)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_sub['Date'], y=df_sub['Total_Consumption'],
                            mode='lines',
                            name='Actual Consumption',
                            line_color="#FFFFFF")) #Line 2
        fig.add_trace(go.Scatter(x=df_sub['Date'], y=df_sub['Predicted_Consumption'],
                            mode='lines',
                            name='Predicted Consumption',
                            line_color="#C6810B")) #Line 3
        fig.add_trace(go.Scatter(x=df_anoms['Date'], y=df_anoms['Total_Consumption'],
                            mode='markers',
                            name='Excess Consumption'))
        fig.update_traces(marker=dict(size=5, 
                                    line=dict(width=5,
                                                color='#C60B0B')))
        fig.update_layout(template='plotly_dark',
                    paper_bgcolor='rgba(0, 0, 0, 0)',
                    plot_bgcolor='rgba(0, 0, 0, 0)',
                    margin={'b': 15},
                    autosize=True,
                    yaxis_title="Consumption (kWh)",
                    xaxis_title="Date",
                    # line_color="#FFFFFF",
                    title={'text': 'Forecasting Electricity Consumption for this year', 'font': {'color': 'white'}, 'x': 0.5})
        return fig

    elif (selected_dropdown_value == 'Appliance-wise Consumption'):
        df_sub = df2

        jan_fridge = df_sub[df_sub['month'] == 'Jan']['Fridge'].values[0]
        feb_fridge = df_sub[df_sub['month'] == 'Feb']['Fridge'].values[0]
        mar_fridge = df_sub[df_sub['month'] == 'Mar']['Fridge'].values[0]
        apr_fridge = df_sub[df_sub['month'] == 'Apr']['Fridge'].values[0]
        may_fridge = df_sub[df_sub['month'] == 'May']['Fridge'].values[0]
        jun_fridge = df_sub[df_sub['month'] == 'Jun']['Fridge'].values[0]
        jul_fridge = df_sub[df_sub['month'] == 'Jul']['Fridge'].values[0]

        jan_kap = df_sub[df_sub['month'] == 'Jan']['Kitchen Appliances'].values[0]
        feb_kap = df_sub[df_sub['month'] == 'Feb']['Kitchen Appliances'].values[0]
        mar_kap = df_sub[df_sub['month'] == 'Mar']['Kitchen Appliances'].values[0]
        apr_kap = df_sub[df_sub['month'] == 'Apr']['Kitchen Appliances'].values[0]
        may_kap = df_sub[df_sub['month'] == 'May']['Kitchen Appliances'].values[0]
        jun_kap = df_sub[df_sub['month'] == 'Jun']['Kitchen Appliances'].values[0]
        jul_kap = df_sub[df_sub['month'] == 'Jul']['Kitchen Appliances'].values[0]

        jan_ac = df_sub[df_sub['month'] == 'Jan']['AC'].values[0]
        feb_ac = df_sub[df_sub['month'] == 'Feb']['AC'].values[0]
        mar_ac = df_sub[df_sub['month'] == 'Mar']['AC'].values[0]
        apr_ac = df_sub[df_sub['month'] == 'Apr']['AC'].values[0]
        may_ac = df_sub[df_sub['month'] == 'May']['AC'].values[0]
        jun_ac = df_sub[df_sub['month'] == 'Jun']['AC'].values[0]
        jul_ac = df_sub[df_sub['month'] == 'Jul']['AC'].values[0]

        jan_wm = df_sub[df_sub['month'] == 'Jan']['Washing Machine'].values[0]
        feb_wm = df_sub[df_sub['month'] == 'Feb']['Washing Machine'].values[0]
        mar_wm = df_sub[df_sub['month'] == 'Mar']['Washing Machine'].values[0]
        apr_wm = df_sub[df_sub['month'] == 'Apr']['Washing Machine'].values[0]
        may_wm = df_sub[df_sub['month'] == 'May']['Washing Machine'].values[0]
        jun_wm = df_sub[df_sub['month'] == 'Jun']['Washing Machine'].values[0]
        jul_wm = df_sub[df_sub['month'] == 'Jul']['Washing Machine'].values[0]

        jan_oap = df_sub[df_sub['month'] == 'Jan']['Other Appliances'].values[0]
        feb_oap = df_sub[df_sub['month'] == 'Feb']['Other Appliances'].values[0]
        mar_oap = df_sub[df_sub['month'] == 'Mar']['Other Appliances'].values[0]
        apr_oap = df_sub[df_sub['month'] == 'Apr']['Other Appliances'].values[0]
        may_oap = df_sub[df_sub['month'] == 'May']['Other Appliances'].values[0]
        jun_oap = df_sub[df_sub['month'] == 'Jun']['Other Appliances'].values[0]
        jul_oap = df_sub[df_sub['month'] == 'Jul']['Other Appliances'].values[0]

        irises_colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)',
                 'rgb(175, 49, 35)', 'rgb(36, 73, 147)']

        fig = go.Figure(data=[go.Pie(
                            name='January 2023',
                            labels = ['Fridge', 'Kitchen Appliances', 'AC', 'Washing Machine', 'Other Appliances'],
                            values = [jan_fridge, jan_kap, jan_ac, jan_wm, jan_oap],
                            marker_colors=irises_colors,
                            hole=0.3
                        ),
                            go.Pie(
                            name='February 2023',
                            labels = ['Fridge', 'Kitchen Appliances', 'AC', 'Washing Machine', 'Other Appliances'],
                            values = [feb_fridge, feb_kap, feb_ac, feb_wm, feb_oap],
                            marker_colors=irises_colors,
                            hole=0.3
                        ),
                        go.Pie(
                            name='March 2023',
                            labels = ['Fridge', 'Kitchen Appliances', 'AC', 'Washing Machine', 'Other Appliances'],
                            values = [mar_fridge, mar_kap, mar_ac, mar_wm, mar_oap],
                            marker_colors=irises_colors,
                            hole=0.3
                        ),
                        go.Pie(
                            name='April 2023',
                            labels = ['Fridge', 'Kitchen Appliances', 'AC', 'Washing Machine', 'Other Appliances'],
                            values = [apr_fridge, apr_kap, apr_ac, apr_wm, apr_oap],
                            marker_colors=irises_colors,
                            hole=0.3
                        ),
                        go.Pie(
                            name='May 2023',
                            labels = ['Fridge', 'Kitchen Appliances', 'AC', 'Washing Machine', 'Other Appliances'],
                            values = [may_fridge, may_kap, may_ac, may_wm, may_oap],
                            marker_colors=irises_colors,
                            hole=0.3
                        ),
                        go.Pie(
                            name='June 2023',
                            labels = ['Fridge', 'Kitchen Appliances', 'AC', 'Washing Machine', 'Other Appliances'],
                            values = [jun_fridge, jun_kap, jun_ac, jun_wm, jun_oap],
                            marker_colors=irises_colors,
                            hole=0.3
                        ),
                        go.Pie(
                            name='July 2023',
                            labels = ['Fridge', 'Kitchen Appliances', 'AC', 'Washing Machine', 'Other Appliances'],
                            values = [jul_fridge, jul_kap, jul_ac, jul_wm, jul_oap],
                            marker_colors=irises_colors,
                            hole=0.3
                        ),
                        ])

        fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=list([
                    dict(label="January",
                        method="update",
                        args=[{"visible": [True, False, False, False, False, False, False]},
                            {"title": "January Consumption Distribution (%) by each Appliance"}]),
                    dict(label="February",
                        method="update",
                        args=[{"visible": [False, True, False, False, False, False, False]},
                            {"title": "February Consumption Distribution (%) by each Appliance",
                                }]),
                    dict(label="March",
                        method="update",
                        args=[{"visible": [False, False, True, False, False, False, False]},
                            {"title": "March Consumption Distribution (%) by each Appliance",
                                }]),
                    dict(label="April",
                        method="update",
                        args=[{"visible": [False, False, False, True, False, False, False]},
                            {"title": "April"}]),
                    dict(label="May",
                        method="update",
                        args=[{"visible": [False, False, False, False, True, False, False]},
                            {"title": "May Consumption Distribution (%) by each Appliance"}]),
                    dict(label="June",
                        method="update",
                        args=[{"visible": [False, False, False, False, False, True, False]},
                            {"title": "June Consumption Distribution (%) by each Appliance"}]),
                    dict(label="July",
                        method="update",
                        args=[{"visible": [False, False, False, False, False, False, True]},
                            {"title": "July Consumption Distribution (%) by each Appliance"}]),
                ]),
            )
        ],
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        title_font_color="#90E219",
        font_color="#90E219",
        width=700,
        height=700,
        )
        return fig

    else:
        trace = []  
        df_sub = df
        trace.append(go.Scatter(x=df_sub.index,
                                y=df_sub['Total_Consumption'],
                                mode='lines',
                                opacity=0.7,
                                name='Time-series Plot of Electricity Consumption for this year',
                                textposition='bottom center',
                                line_color="#FFFFFF",) ) #Line 1  
        traces = [trace]
        data = [val for sublist in traces for val in sublist]
        figure = {'data': data,
                'layout': go.Layout(
                    colorway=["#5E0DAC"],
                    template='plotly_dark',
                    paper_bgcolor='rgba(0, 0, 0, 0)',
                    plot_bgcolor='rgba(0, 0, 0, 0)',
                    margin={'b': 15},
                    hovermode='x',
                    autosize=True,
                    yaxis_title="Consumption (kWh)",
                    xaxis_title="Date",
                    title={'text': 'Electricity Consumption for this year', 'font': {'color': 'white'}, 'x': 0.5},
                    xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
                 
                ),

                }

        return figure
        


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)