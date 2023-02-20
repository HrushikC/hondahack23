# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from fruitgraph import generate_fruit_graph, generateHeatmap, generateAverageSpeedOfDrivers

app = Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "DATA I/O 2022"
server = app.server


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("/Users/hrushik/Desktop/Data-IO-2022/data/FinalCleanedDataIO.csv") # had to use full path for some reason

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H4("Data I/O 2022", className="app__header__title"),
                        html.P(
                            "Analytics Dashboard for the honda dataset.",
                            className="app__header__title--grey",
                        ),
                    ],
                    className="app__header__desc column"
                )
            ],
            className="app__header"
        ),
        html.Div(
            [
                html.Div(
                    [
                        # Big graph
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dcc.Dropdown(
                                                    df.columns.unique(),
                                                    "device",
                                                    id="xaxis-column",
                                                ),
                                                dcc.RadioItems(
                                                    ["Linear", "Log"], "Linear", id="xaxis-type", inline=True
                                                ),
                                            ],
                                            style={"width": "48%", "display": "inline-block"},
                                        ),
                                        html.Div(
                                            [
                                                dcc.Dropdown(
                                                    df.columns.unique(),
                                                    "device",
                                                    id="yaxis-column",
                                                ),
                                                dcc.RadioItems(
                                                    ["Linear", "Log"], "Linear", id="yaxis-type", inline=True
                                                ),
                                            ],
                                            style={"width": "48%", "float": "right", "display": "inline-block"},
                                        ),
                                    ]
                                ),
                                dcc.Graph(id="indicator-graphic"),
                            ],
                            className="graph__container padding__right"
                        ),
                        html.Div(
                            [
                                generateAverageSpeedOfDrivers(pd,px,dcc),
                            ],
                            className="graph__container"
                        ),
                    ],
                    className="column"
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                generateHeatmap(pd,px,dcc),
                            ],
                            className="graph__container"
                        ),
                        html.Div(
                            [
                                generate_fruit_graph(pd,px,dcc),
                            ],
                            className="graph__container"
                        ),
                    ],
                    className="column"
                ),
            ],
            className="app__content"
        ),
    ],
    className="app__container"
)

@app.callback(
    Output("indicator-graphic", "figure"),
    Input("xaxis-column", "value"),
    Input("yaxis-column", "value"),
    Input("xaxis-type", "value"),
    Input("yaxis-type", "value"),
)
def update_graph(xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type):
    filterDF = df[[xaxis_column_name, yaxis_column_name]]

    fig = px.scatter(
        filterDF,
        x=xaxis_column_name,
        y=yaxis_column_name,
    )

    fig.update_layout(margin={"l": 40, "b": 40, "t": 10, "r": 0}, hovermode="closest")

    fig.update_xaxes(
        title=xaxis_column_name, type="linear" if xaxis_type == "Linear" else "log"
    )

    fig.update_yaxes(
        title=yaxis_column_name, type="linear" if yaxis_type == "Linear" else "log"
    )

    return fig


# if __name__ == '__main__':
#     app.run_server(debug=True)
