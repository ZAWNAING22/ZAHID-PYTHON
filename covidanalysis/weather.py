import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#fake 10 yers data
np.random.seed(42)
years=np.arange(2010,2020)
months=np.arange(1,13)
data=[]

for year in years:
    for month in months:
        avg_temp=np.random.normal(loc=20, scale=10) #C
        rainfall=np.random.normal(loc=100, scale=10) #mm
        humidity=np.random.normal(loc=65, scale=15) #s
        data.append([year,month,avg_temp,rainfall,humidity])
df=pd.DataFrame(data, columns=['year','month','avg_temp','rainfall','humidity'])
print(df)
print("\n data statistics: ")
print(df.head())  
print(df.describe())  

#Data visualization
yearly_temp=df.groupby("year")["avg_temp"].mean()
print(yearly_temp)
plt.figure(figsize=(8,4))
plt.plot(yearly_temp.index, yearly_temp.values, marker='o', color='orange', linestyle='--')
plt.title("Average Yearly Temperature (2010–2019")
plt.xlabel("Year")
plt.ylabel("average temperature")
plt.grid(True)
plt.show()

#Step 4: Monthly Rainfall Pattern
monthly_rainfall=df.groupby("month")['rainfall'].mean()
plt.figure(figsize=(10,5))
plt.bar(monthly_rainfall.index, monthly_rainfall.values, color='skyblue')
plt.title("Average Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.xticks(months)
plt.show()

#Step 5: Scatter Plot (Humidity vs Temperature)
plt.figure(figsize=(8,5))
plt.scatter(df["humidity"], df["avg_temp"], alpha=0.6, color='green')
plt.title("Humidity vs. Average Temperature")
plt.xlabel("Humidity (%)")
plt.ylabel("Avg Temp (°C)")
plt.grid(True)
plt.show()


