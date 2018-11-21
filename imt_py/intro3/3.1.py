import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

complaints = pd.read_csv('extract.csv')

complaint_type_column = complaints['Complaint Type']

print(complaints[:5])
print(complaints[['Complaint Type', 'Borough']][:10])
print(complaints['Complaint Type'].value_counts())
print(complaints['Complaint Type'].value_counts().plot(kind='bar'))

plt.savefig('./plot.pdf')