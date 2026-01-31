import matplotlib.pyplot as plt

plt.pie(
    x=[10, 20, 30, 40],
    labels=['A', 'B', 'C', 'D']
)
plt.waitforbuttonpress()