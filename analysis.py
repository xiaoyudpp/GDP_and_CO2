
from altair.vegalite.v4.schema.core import Data
import pandas as pd

# import data
data = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

import altair as alt
import numpy as np

GDPcap = data["GDP per capita (constant 2010 US$)"]
data["Log GDP Per Capita"] = np.log(GDPcap)
my_chart = (
    alt.Chart(data)
    .mark_circle(size=50)
    .encode(
        x="Log GDP Per Capita",
        y="Mortality rate, infant (per 1,000 live births)",
        tooltip="Country Name",
    )
)
my_chart