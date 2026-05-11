import pandas as pd
from dash import Dash ,dcc ,html
import plotly.express as px

df=pd.read_csv("formatted_output.csv")
df["date"]=pd.to_datetime(df["date"])
df=df.sort_values("date")
df=df.groupby("date")["sales"].sum().reset_index()

app= Dash(__name__)

fig=px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)
app.layout = html.Div([

    html.H1("Soul Foods Sales Dashboard"),
    dcc.Graph(figure=fig)
])
if __name__ == "__main__" :
    app.run(debug=True)