import matplotlib.pyplot as plt
import seaborn as sns
from pandas import read_csv
 
fighter_data = read_csv('Cleaned Fighter Data - Sheet1.csv')
fighter_data = fighter_data[['class', 'height']]
print(fighter_data)
 
 
plt.figure(figsize=(7, 7))
ax = sns.boxplot(x='class', y='height', data=fighter_data)
plt.title("UFC Fighter Heights By Weight Class")
plt.xticks(rotation=45)
plt.xlabel('Weight Class')
plt.ylabel('Height (Inches)')
plt.tight_layout()
plt.grid(True)
 
plt.show()