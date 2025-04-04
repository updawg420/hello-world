import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

PCollege_Sal_Data = pd.read_csv('final-post-college-salaries.csv')
PCollege_Sal_Data = PCollege_Sal_Data.drop(columns=['Rank'], axis=1)

# print(PCollege_Sal_Data.shape)
# list & rename columns
# PCollege_Sal_Data.columns
# PCollege_Sal_Data.columns = ['Rank', 'Major_code', 'Major', 'Total', 'Sample_size', 'Median', 'P25th_percentile',
#                               'P75th_percentile', 'P90th_percentile', 'P95th_percentile', 'Unemployment_rate',
#                               'Employment_rate']