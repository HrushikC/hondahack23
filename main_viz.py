colors = {
    "graph_bg": "#FFFFFF",
    "text": "#000000",
    "graph_line": "#107ACE"
    }

DATA_PATH = './data/FinalCleanedDataIO.csv'
NEW_DATA_PATH = './data/route_summary.csv'

def line_map(pd, px, dcc):
    # import plotly.express as px
    df = px.data.gapminder().query("year == 2007")
    fig = px.line_geo(df, locations="iso_alpha",
                    color="continent", # "continent" is one of the columns of gapminder
                    projection="orthographic")
    return dcc.Graph(
        figure=fig
    )
    # fig.show()
    # df = pd.read_csv(DATA_PATH)
    # df['dayofweek'] = pd.to_datetime(df['utctime(datetime)']).dt.day_name()
    # data = df.groupby(['dayofweek'])["avgspeed"].mean()

    # fig = px.bar(data)
    # fig.update_layout(
    #     plot_bgcolor=colors['graph_bg'],
    #     paper_bgcolor=colors['graph_bg'],
    #     font_color=colors['text']
    # )
    # return dcc.Graph(
    #     figure=fig
    # )

def generateHeatmap(pd, px, dcc):
    df = pd.read_csv(DATA_PATH)

    fig = px.density_mapbox(df, lat='endlatitude', lon='endlongitude', mapbox_style="stamen-terrain")
 
    fig.update_layout(
        plot_bgcolor=colors['graph_bg'],
        font_color=colors['text']
    )
    return dcc.Graph(
        figure=fig
    )

def generateAverageSpeedOfDrivers(pd, px, dcc):
    df = pd.read_csv(DATA_PATH)

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
        figure=fig
    )
    return