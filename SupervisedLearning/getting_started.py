import numpy as np

data = np.loadtxt(open("data/liver_data.txt", "rb"), delimiter = ",")

alcohol_consumption = data[:, 5]
print(alcohol_consumption)