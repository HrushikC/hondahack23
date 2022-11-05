from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

app = Dash(__name__)

df = pd.read_csv("../data/FinalCleanedDataIO.csv")

app.layout = html.Div(
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
    ]
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


if __name__ == "__main__":
    app.run_server(debug=True)
