import matplotlib.pyplot as plt
import pandas as pd

grh = pd.read_csv("data.csv", names=("x", "y"))
print(grh)

x = grh["x"]
y = grh["y"]

plt.plot(x, y)
plt.savefig("sample.jpg")