import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('Stud_marks.csv')

# Find highest marks and student name
max_marks = data['sub1_m'].max()
topper_name = data.loc[data['sub1_m'] == max_marks, 'name'].values[0]

# Print result
print(f"Highest marks in Subject 1: {max_marks}, scored by {topper_name}")

# Simple bar chart for Subject 1
plt.bar(data['name'], data['sub1_m'])
plt.title("Subject 1 Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()
