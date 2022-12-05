# Задача 1. Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

from matplotlib import pyplot as plt

x = []
y = []
for i in range(-15, 15):
    x.append(i)

for i in range(len(x)):
    y.append(5 * x[i] * x[i] + 10 * x[i] - 30)

plt.plot(x, y)

plt.title("Line graph")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

print('Значение функции отрицательно при х = 1.6 и меньше')
