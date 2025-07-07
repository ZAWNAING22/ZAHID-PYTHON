import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data samples

np.random.seed(0)
Dates=pd.date_range(start='2022-01-01',periods=10)
Cases=np.random.randint(100,1000,10)
df=pd.DataFrame({'Dates':Dates,
                 'Daily_Cases':Cases})

#Data analyssis
print(df.head())
print("\n Statistic summary")
print(df['Daily_Cases'].describe())

#Data visualization
plt.figure(figsize=(10,5))
plt.plot(df['Dates'], df['Daily_Cases'], marker='o', color='teal', linestyle='--')
plt.title('Daily COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
