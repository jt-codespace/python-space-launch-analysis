import pandas as pd
import matplotlib.pyplot as plt

# Space launch dataset
data = {
    "Country": ["USA", "India", "China", "Russia", "India"],
    "Launches": [120, 35, None, 60, 35]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values with 0
df["Launches"] = df["Launches"].fillna(0)

print("\nCleaned Data")
print(df)

plt.bar(df["Country"], df["Launches"])

plt.title("Space Launch Analysis")
plt.xlabel("Country")
plt.ylabel("Number of Launches")

plt.show()
