import pandas as pd
import plotly_express as px
import csv

df = pd.read_csv("data.csv")

mean = df.groupby("level")["attempt"].mean()
print(mean)

as_index = False

fig = px.scatter(mean, x="student_id", y="level",
                    size="attempt", color="attempt",
                        size_max=60)

fig.show()