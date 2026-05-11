import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Country": ["USA", "India", "China", "Russia"],
    "Launches": [120, 35, 80, 60]
}


df = pd.DataFrame(data)

print(df)

plt.bar(df["Country"],df["Launches"])
plt.title("Space Launch Analysis")
plt.xlabel("Country")
plt.ylabel("Number Of Launches")
plt.show()
