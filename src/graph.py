import numpy as np
import matplotlib.pyplot as plt

# sin波
# x = np.arange(-5, 5, 0.1)
# y = np.sin(x)

# plt.plot(x, y)
# # plt.show() # グラフ描画(うまくいかない)
# plt.savefig("sample.jpg")


# 折れ線グラフ
# data = [2, 5, 10, 2, 6]
# data2 = [10, 4, 1, 3, 4]
# plt.plot(data, "red", marker="o")
# plt.plot(data2, "blue", marker="^")
# plt.savefig("sample.jpg")


# 散布図
x = [10, 51, 44, 23, 55, 95]
y = [5, 125, 2, 55, 19, 55]
plt.scatter(x, y, color="blue", marker="s")
plt.savefig("sample.jpg")