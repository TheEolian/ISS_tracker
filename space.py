import pandas as pd
import plotly.express as px

#add json API

url = 'http://api.open-notify.org/iss-now.json'
df = pd.read_json(url)

#create latitude and logitude as colums with iss_position

df['latitude'] = df.loc['latitude','iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)

#remove index and message columns as they are unneccessary and now easier to plot
df = df.drop(['index', 'message'], axis=1)
