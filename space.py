import pandas as pd
import plotly.express as px

# add API in json

url = 'http://api.open-notify.org/iss-now.json'
df = pd.read_json(url)

# create latitude and longitude as columns

df['latitude'] = df.loc['latitude','iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)

# remove index and message columns
df = df.drop(['index', 'message'], axis=1)

# use plotly to plot the latitude and longitude on global map

fig = px.scatter_geo(df, lat='latitude', lon='longitude')

fig.show()
