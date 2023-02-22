def get_layout(pd, go, dcc, html):
    df = pd.read_csv("./data/route_summary.csv")
    df = df.drop(
        columns=[
            "start_ts",
            "end_ts",
            "trip_start_lat",
            "trip_start_lon",
            "trip_end_lat",
            "trip_end_lon",
            "id",
            "vehicle_id",
            "driver_id",
            "status",
        ]
    )
    layout = html.Div(
        [
            html.H4("Scatter Plot with Dynamic Axis Selection"),
            html.Div(
                [
                    dcc.Dropdown(
                        id="xaxis",
                        options=[
                            {"label": col, "value": col} for col in df.columns[1:]
                        ],
                        value=df.columns[0],
                    ),
                    dcc.Dropdown(
                        id="yaxis",
                        options=[
                            {"label": col, "value": col} for col in df.columns[1:]
                        ],
                        value=df.columns[1],
                    ),
                ],
                style={"width": "50%", "display": "inline-block"},
            ),
            dcc.Graph(id="graph"),
        ]
    )
    return layout

# Define the function that calculates the linear regression line
def calc_regression(x, y, np, linregress):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    line_x = np.array([min(x), max(x)])
    line_y = slope * line_x + intercept
    return line_x, line_y, r_value


# Define the function that updates the scatter plot
def update_figure(xaxis, yaxis, pd, go, np, linregress):
    df = pd.read_csv("./data/route_summary.csv")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df[xaxis], y=df[yaxis], mode="markers"))
    line_x, line_y, r_value = calc_regression(df[xaxis], df[yaxis], np, linregress)
    fig.add_trace(go.Scatter(x=line_x, y=line_y, mode="lines", line=dict(color="red")))
    fig.update_layout(
        title="Scatter Plot with Dynamic Axis Selection and Linear Regression",
        xaxis_title=xaxis,
        yaxis_title=yaxis,
        annotations=[
            dict(
                x=0.95,
                y=0.05,
                xanchor="right",
                yanchor="bottom",
                text="Correlation: {:.2f}".format(r_value),
                showarrow=False,
            )
        ],
    )
    x_range = [-10, df[xaxis].max() * 1.05]
    y_range = [-10, df[yaxis].max() * 1.05]
    fig.update_xaxes(range=x_range)
    fig.update_yaxes(range=y_range)
    return fig