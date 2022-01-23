import numpy as np
from pandas import Series, DataFrame
import pandas as pd

import webbrowser
website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
# webbrowser.open(website)

nfl_frame = pd.read_clipboard()

print(nfl_frame)
print(nfl_frame.columns)
print(nfl_frame['First Season'])
print(nfl_frame.Team)