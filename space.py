import pandas as pd
import plotly.express as px

#add json API

url = 'http://api.open-notify.org/iss-now.json'
df = pd.read_json(url)
