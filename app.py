from dash import Dash, html, dcc, Input, Output

# Initialize the Dash app
app = Dash(__name__)

# Layout of the app
app.layout = html.Div(
    [
        html.H1("Let's test the continuous deployment"),
        html.Div(id="output-div", children="Button not clicked yet."),
        html.Button("Click Me", id="example-button", n_clicks=0),
    ]
)


# Callback to update the text on button click
@app.callback(Output("output-div", "children"), Input("example-button", "n_clicks"))
def update_output(n_clicks):
    return f"Button clicked {n_clicks} times."


# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8050", debug=True)
