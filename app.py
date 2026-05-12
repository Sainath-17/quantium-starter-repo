import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Read CSV file
df = pd.read_csv("formatted_output.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Create Dash app
app = Dash(__name__)

# App Layout
app.layout = html.Div([

    html.H1(
        "Soul Foods Sales Dashboard",
        id="header",
        style={
            "textAlign": "center",
            "color": "#2c3e50",
            "marginBottom": "30px"
        }
    ),

    dcc.RadioItems(

        id="region-selector",

        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"}
        ],

        value="all",

        inline=True,

        style={
            "textAlign": "center",
            "marginBottom": "20px",
            "fontSize": "18px"
        }

    ),

    dcc.Graph(id="sales-chart")

],
style={
    "padding": "20px",
    "fontFamily": "Arial",
    "backgroundColor": "#f4f6f7"
})

# Callback to update chart
@app.callback(

    Output("sales-chart", "figure"),

    Input("region-selector", "value")

)
def update_chart(selected_region):

    # Filter region
    if selected_region == "all":
        filtered_df = df

    else:
        filtered_df = df[df["region"] == selected_region]

    # Group sales by date
    grouped_df = filtered_df.groupby("date")["sales"].sum().reset_index()

    # Create line chart
    fig = px.line(
        grouped_df,
        x="date",
        y="sales",
        title=f"{selected_region.capitalize()} Region Sales Over Time"
    )

    # Improve chart appearance
    fig.update_layout(
        title_x=0.5,
        plot_bgcolor="white",
        paper_bgcolor="#f4f6f7",
        xaxis_title="Date",
        yaxis_title="Sales",
        font=dict(size=14)
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)