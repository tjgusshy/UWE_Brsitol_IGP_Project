import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as matplot

xls = pd.ExcelFile('csv_data/data1.xlsx')
demo_df = pd.read_excel(xls,'Demographics')
demo_df

