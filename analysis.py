import pandas as pd

print("Data Analysis Practice Started")

# Read CSV file
df = pd.read_csv("student.csv")

print("\nFull Dataset:")
print(df)

# Basic statistics
print("\nAverage Marks in Each Subject:")
print(df.mean(numeric_only=True))

print("\nHighest Math Score:")
print(df["Math"].max())

print("\nLowest Science Score:")
print(df["Science"].min())

print("\nTotal Marks of Each Student:")
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
print(df[["Student", "Total"]])