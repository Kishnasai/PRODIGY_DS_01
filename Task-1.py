import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as px



df = pd.read_csv(r"C:\Users\dundi\OneDrive\Desktop\population_data.csv", names=['countries', 'UK', 'India', 'China', 'Russia', 'USA', 'Pakistan', 'Japan', 'Bangladesh', 'Australia'])
display(df.head(21))



plt.figure(figsize=(10, 6))
plt.bar(df['countries'], df['India'])
plt.xlabel('Years --------->')
plt.ylabel('Population (Millions) --------->')
plt.title('Bar Chart')
plt.grid(True)
plt.tight_layout()
plt.show()



plt.figure(figsize=(14, 6))
sns.lineplot(x='countries', y='UK', data=df)
plt.xlabel('Years --------->')
plt.ylabel('Population (Millions) --------->')
plt.title("Line Chart")
plt.show()



plt.figure(figsize=(16, 6))
plt.scatter(df['countries'], df['Russia'])
plt.title("Scatter Plot")
plt.xlabel('Years  --------->')
plt.ylabel('Population  --------->')
plt.colorbar() 
plt.show()



plt.figure(figsize=(14, 6))
plt.scatter(df['countries'], df['Pakistan'])
plt.title("Scatter Plot")
plt.xlabel('Years --------->')
plt.ylabel('Population (Millions) --------->')
plt.show()



plt.figure(figsize=(14, 6))
plt.plot(df['USA'])
plt.title("Scatter Plot")
plt.xlabel('Years --------->')
plt.ylabel('Population (Millions) --------->')
plt.show()



plt.figure(figsize=(12, 4))
plt.hist(df['China'])
plt.xlabel('Years --------->')
plt.ylabel('Population (Millions) --------->')
plt.title("Histogram")
plt.show()
