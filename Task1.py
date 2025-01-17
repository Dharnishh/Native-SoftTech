import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load a publicly available dataset, for example, the Titanic dataset from Seaborn
df = sns.load_dataset('titanic')


# Filter passengers who survived
survived_passengers = df[df['survived'] == 1]


# Group by class and calculate the average fare
avg_fare_per_class = df.groupby('class')['fare'].mean()
print(avg_fare_per_class)


# Plot the trend of fare over age
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='age', y='fare')
plt.title('Fare over Age')
plt.show()


# Bar chart of average fare per class
plt.figure(figsize=(8, 6))
avg_fare_per_class.plot(kind='bar')
plt.title('Average Fare per Class')
plt.xlabel('Class')
plt.ylabel('Average Fare')
plt.show()
