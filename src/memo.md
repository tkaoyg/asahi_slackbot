https://github.com/scrapinghub/slackbot
slackbot ライブラリ(Github)

slackbotの中のbot.pyを使用

https://miyabikno-jobs.com/entrance-labotlatori/
↑を参考に作成

'''python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

grh = pd.read_csv("data.csv", names=("x", "y"))

x = grh["x"]
y = grh["y"]

plt.plot(y, x)
plt.savefig("sample.jpg")

'''
