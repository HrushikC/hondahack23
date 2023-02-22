colors = {
    "graph_bg": "#FFFFFF",
    "text": "#000000",
    "graph_line": "#107ACE"
    }

# DATA_PATH = './data/FinalCleanedDataIO.csv'
ROUTE_DATA_PATH = './data/route_summary.csv'
TRIP_DATA_PATH = './data/trip_requests.csv'

# def line_map(pd, px, dcc):
#     # import plotly.express as px
#     df = px.data.gapminder().query("year == 2007")
#     fig = px.line_geo(df, locations="iso_alpha",
#                     color="continent", # "continent" is one of the columns of gapminder
#                     projection="orthographic")
#     return dcc.Graph(
#         figure=fig
#     )


def bubble_chart(pd, px, dcc):
    df = pd.read_csv(ROUTE_DATA_PATH)

    fig = px.scatter(df, x="trip_distance_miles", y="mins_travelled",
                size="avg_speed_mph", color="make", log_x=True, size_max=60)
    return dcc.Graph(
        figure=fig
    )

def month_box(pd, px, dcc):
    df = px.data.tips()
    df = pd.read_csv(ROUTE_DATA_PATH)
    df['start_ts'] = pd.to_datetime(df['start_ts'])
    df["month"] = pd.DatetimeIndex(df["start_ts"]).month_name()

    fig = px.scatter(df, x="avg_speed_mph", y="trip_distance_miles", color="make", facet_col="month",
                    marginal_x="box")
    return dcc.Graph(
        figure=fig
    )

def map_scatter(pd, px, dcc):
    df = pd.read_csv(ROUTE_DATA_PATH)

    # fig = px.density_mapbox(df, lat='trip_start_lat', lon='trip_start_lon', mapbox_style="stamen-terrain", opacity=0.7)
    fig = px.scatter_mapbox(df, lat='trip_start_lat', lon='trip_start_lon', color_discrete_sequence=["#6d6e6e"], zoom=10, height=550)

    fig.update_layout(
        mapbox_style="open-street-map", # stamen-terrain
        margin={"r":0,"t":0,"l":0,"b":0},
        plot_bgcolor=colors['graph_bg'],
        font_color=colors['text']
    )

    return dcc.Graph(
        figure=fig
    )

def day_box_plot(go, pd, np, dcc):
    df = pd.read_csv(ROUTE_DATA_PATH)

    x_data = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    df['start_ts'] = pd.to_datetime(df['start_ts'])

    y0 = df[df['start_ts'].dt.dayofweek == 0]['trip_distance_miles']
    y1 = df[df['start_ts'].dt.dayofweek == 1]['trip_distance_miles']
    y2 = df[df['start_ts'].dt.dayofweek == 2]['trip_distance_miles']
    y3 = df[df['start_ts'].dt.dayofweek == 3]['trip_distance_miles']
    y4 = df[df['start_ts'].dt.dayofweek == 4]['trip_distance_miles']
    y5 = df[df['start_ts'].dt.dayofweek == 5]['trip_distance_miles']
    y6 = df[df['start_ts'].dt.dayofweek == 6]['trip_distance_miles']

    y_data = [y0, y1, y2, y3, y4, y5, y6]

    colors = ['rgba(93, 164, 214, 0.5)', 'rgba(255, 144, 14, 0.5)', 'rgba(44, 160, 101, 0.5)',
            'rgba(255, 65, 54, 0.5)', 'rgba(207, 114, 255, 0.5)', 'rgba(127, 96, 0, 0.5)']

    fig = go.Figure()

    for xd, yd, cls in zip(x_data, y_data, colors):
            fig.add_trace(go.Box(
                y=yd,
                name=xd,
                boxpoints='all',
                jitter=0.5,
                whiskerwidth=0.2,
                fillcolor=cls,
                marker_size=2,
                line_width=1)
            )

    fig.update_layout(
        title='Trip Distance by day of week',
        yaxis=dict(
            autorange=True,
            showgrid=True,
            zeroline=True,
            dtick=5,
            gridcolor='rgb(255, 255, 255)',
            gridwidth=1,
            zerolinecolor='rgb(255, 255, 255)',
            zerolinewidth=2,
        ),
        margin=dict(
            l=40,
            r=30,
            b=80,
            t=100,
        ),
        paper_bgcolor='rgb(243, 243, 243)',
        plot_bgcolor='rgb(243, 243, 243)',
        showlegend=False
    )

    return dcc.Graph(
        figure=fig
    )