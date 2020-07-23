import matplotlib.pyplot as plt
x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=200)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 7, 0, 345])
plt.show()