import matplotlib.pyplot as plt

plt.title('Cube Numbers', fontsize=20)
plt.xlabel('value', fontsize=10)
plt.ylabel('Cube of value', fontsize=10)
plt.tick_params(axis='both', labelsize=10)
x_values = list(range(1001))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
plt.show()
