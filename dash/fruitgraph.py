colors = {
    "graph_bg": "#FFFFFF",
    "text": "#000000",
    "graph_line": "#107ACE"
    }

def generate_fruit_graph(pd, px, dcc):
    df = pd.read_csv('../data/FinalCleanedDataIO.csv')
    df['dayofweek'] = pd.to_datetime(df['utctime(datetime)']).dt.day_name()
    data = df.groupby(['dayofweek'])["avgspeed"].mean()

    fig = px.bar(data)
    fig.update_layout(
        plot_bgcolor=colors['graph_bg'],
        paper_bgcolor=colors['graph_bg'],
        font_color=colors['text']
    )
    return dcc.Graph(
        figure=fig
    )

def generateHeatmap(pd, px, dcc):
    df = pd.read_csv('../data/FinalCleanedDataIO.csv')

    fig = px.density_mapbox(df, lat='endlatitude', lon='endlongitude', mapbox_style="stamen-terrain")
 
    fig.update_layout(
        plot_bgcolor=colors['graph_bg'],
        font_color=colors['text']
    )
    return dcc.Graph(
        id='example-graph',
        figure=fig
    )

def generateAverageSpeedOfDrivers(pd, px, dcc):
    df = pd.read_csv('../data/FinalCleanedDataIO.csv')

    df2 = df.groupby(['device'])['avgspeed_mph'].mean()
    dfUnder = df2[df2<=25]
    dfAvg = df2[df2<=45]
    dfAvg = dfAvg[dfAvg>25]
    dfOver = df2[df2>45]
    dfFinal = [['UnderThresholdSpeed <= 25 mph',dfUnder.count() ],['BetweenThresholdSpeed > 25 mph <= 45 mph',dfAvg.count()], ['OverThresholdSpeed > 45 mph',dfOver.count() ]]
    dffinalDF = pd.DataFrame(dfFinal, columns=['Thresholds', 'Count'])


    fig = px.bar(dffinalDF, x = 'Thresholds', y = 'Count')
    fig.update_layout(
        plot_bgcolor=colors['graph_bg'],
        font_color=colors['text']
    )
    return dcc.Graph(
        id='example-graph',
        figure=fig
    )