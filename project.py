import plotly.figure_factory as pf
import pandas as pd

data = pd.read_csv("data.csv")

fig = pf.create_distplot([data["Weight(Pounds)"].tolist()],["number"],show_hist= False)
fig.show()