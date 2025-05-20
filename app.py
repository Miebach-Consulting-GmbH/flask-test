from dash import Dash, html, dcc, Input, Output
import os

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


def get_counter():
    """Read and return the persisted counter value."""
    if os.path.exists("counter.txt"):
        with open("counter.txt", "r") as fh:
            try:
                return int(fh.read().strip())
            except ValueError:
                return 0
    return 0


def set_counter(n: int) -> None:
    """Persist the counter value to disk."""
    with open("counter.txt", "w") as fh:
        fh.write(str(n))


# Callback to update the text on button click
@app.callback(Output("output-div", "children"), Input("example-button", "n_clicks"))
def update_output(n_clicks):
    previous = get_counter()
    total = previous + (n_clicks or 0)
    set_counter(total)
    return f"Button clicked {total} times. (previous counter: {previous})"


# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8050", debug=True)
