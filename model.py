# 1-9-2023 Harini Nippani

#This is where I will be creating the analysis model. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('parental_leave.csv')
data_sorted = data.sort_values(by='Paid Maternity Leave', ascending=False)
top = data_sorted.head(20)

#plot the figure "canvas" for the graph
plt.figure(figsize=(10, 6))
#chanage the barh to other types of graphs if you want
plt.barh(top['Industry'], top['Paid Maternity Leave'], color='pink')
#used to plot the grsph. like a print statment
plt.show()