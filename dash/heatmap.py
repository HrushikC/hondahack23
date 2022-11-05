colors = {
    "graph_bg": "#0b53c8",
    "text": "#0b83c8",
    "graph_line": "#107ACE"
    }

def generateHeatmap(pd, px, dcc):
    df = pd.read_csv('/Users/akhildamarla/Desktop/FinalCleanedDataIO.csv')

    fig = px.density_mapbox(df, lat='endlatitude', lon='endlongitude', mapbox_style="stamen-terrain")
 
    fig.update_layout(
        plot_bgcolor=colors['graph_bg'],
        font_color=colors['text']
    )
    return dcc.Graph(
        id='example-graph',
        figure=fig
    )