import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# Create the Dash app
app = dash.Dash()

# Create a scatter plot
fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)

# Add the plot to the Dash app
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

# Run the Dash app
app.run_server()
