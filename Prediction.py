#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# The Salary Dataset contains 763 rows and 6 columns with the following data:
# 1. Rank
# 2. Major
# 3. Degree Type
# 4. Early Career Pay
# 5. Mid-Career Pay
# 6. High Meaning Percentage

PCollege_Sal_Data = pd.read_csv('final-post-college-salaries.csv')
PCollege_Sal_Data = PCollege_Sal_Data.drop(columns=['Rank'], axis=1)

# print(PCollege_Sal_Data.shape)
# list & rename columns
# PCollege_Sal_Data.columns
# PCollege_Sal_Data.columns = ['Rank', 'Major_code', 'Major', 'Total', 'Sample_size', 'Median', 'P25th_percentile',
#                               'P75th_percentile', 'P90th_percentile', 'P95th_percentile', 'Unemployment_rate',
#                               'Employment_rate']