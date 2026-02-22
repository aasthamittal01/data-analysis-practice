import pandas as pd

print("Data Analysis Practice Started")

data = {
    "Student": ["A", "B", "C", "D"],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print("\nDataset:")
print(df)

print("\nAverage Marks:")
print(df["Marks"].mean())