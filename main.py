import matplotlib.pyplot as plt
import csv

x1 = []
y1 = []
x2 = x1
y2 = []

with open('data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append(int(row[0]))
        y1.append(int(row[1]))
        y2.append(int(row[2]))

plt.plot(x1, y1, label="leftFlyWheel")
plt.plot(x2, y2, label="rightFlyWheel")
plt.xlabel('Time in MSec')
plt.ylabel('RPM of Flywheels')
plt.title('Flywheels Without Disc Fired')
plt.legend()
plt.show()

