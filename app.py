# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, html, Input, Output
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import linregress

import dynamicGraph
from main_viz import map_scatter, day_box_plot, month_box, bubble_chart

app = Dash(
    __name__,
    meta_tags=[{"name": "viewport",
                "content": "width=device-width, initial-scale=1"}],
)
app_heading = "Honda Data Challenge 2023"
graph_container = "graph__container"

app.title = app_heading
server = app.server


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# had to use full path for some reason
# df = pd.read_csv("./data/FinalCleanedDataIO.csv")

app.layout = \
    html.Div([
        html.Div([
            html.Div([
                html.H4(app_heading,
                        className="app__header__title"
                        ),
                html.P(
                    "Analytics Dashboard for the honda dataset.",
                    className="app__header__title--grey",
                ),
            ], className="app__header__desc column"
            )
        ], className="app__header"
        ),
        html.Div(
            [
            map_scatter(pd, px, dcc),
        ], className=graph_container
        ),
        html.Div([
            html.Div([
                html.Div([
                    dynamicGraph.get_layout(pd, go, dcc, html),
                ], className=graph_container
                ),
            ], className="column"
            ),
            html.Div([
                html.Div([
                    day_box_plot(go, pd, np, dcc),
                ], className=graph_container
                ),
            # html.Div(
            #     [
            #         bubble_chart(pd, px, dcc),
            #     ], className=graph_container
            # ),
            ], className="column"
            ),
        ], className="app__content"
        ),
        html.Div(
            [
                month_box(pd, px, dcc),
            ], className=graph_container
        ),
    ], className="app__container"
    )

# Define the callbacks
@app.callback(
    Output("graph", "figure"), [
        Input("xaxis", "value"), Input("yaxis", "value")]
)
def update_graph(xaxis, yaxis):
    fig = dynamicGraph.update_figure(xaxis, yaxis, pd, go, np, linregress)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
