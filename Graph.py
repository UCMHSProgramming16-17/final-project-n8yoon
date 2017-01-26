import numpy as np
import pandas as pd

from bokeh.plotting import figure, output_file, save
from bokeh.charts import Line, output_file, save

import csv

df = pd.read_csv('Demographics.csv')

data = Line(df, x = 'JURISDICTION NAME', y = 'COUNT PARTICIPANTS', title = 'Demographics Statistics by Zip Code')

output_file('Demographics.html')

save(data)
