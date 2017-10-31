import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('movie_metadata.csv')  #Load CSV into dataframe

#df1 = df[['actor_2_name','gross']]  #Only want Main Actor and Gross $

df2 = df[['gross','title_year']]  #Only want year and gross$

#print df2.head() # Print first 5
#print df2.tail() # Print last 5
#print df2.describe()

#plt.figure(figsize = (15,5))
#plt.plot(df2['gross'])

#df['gross'].replace('', np.nan, inplace=True)
#df.dropna(subset=['gross'], inplace=True)

#print df.tail(10)
plt.title('Movie Grossage Over Time')
x = df['title_year']
y = df['gross']
plt.scatter(x,y, s = 5)
plt.show()
