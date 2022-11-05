colors = {
    "graph_bg": "#0b53c8",
    "text": "#0b83c8",
    "graph_line": "#107ACE"
    }

def generate_fruit_graph(pd, px, dcc):
    df = pd.read_csv('../v2x_data/FinalCleanedDataIO.csv')
    df['dayofweek'] = pd.to_datetime(df['utctime(datetime)']).dt.day_name()
    data = df.groupby(['dayofweek'])["avgspeed"].mean()

    fig = px.bar(data)
    fig.update_layout(
        plot_bgcolor=colors['graph_bg'],
        font_color=colors['text']
    )
    return dcc.Graph(
        id='example-graph',
        figure=fig
    )
