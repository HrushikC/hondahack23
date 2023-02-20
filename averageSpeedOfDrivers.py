colors = {
    "graph_bg": "#0b53c8",
    "text": "#0b83c8",
    "graph_line": "#107ACE"
    }

DATA_PATH = '/data/FinalCleanedDataIO.csv'

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
        id='example-graph',
        figure=fig
    )