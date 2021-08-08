
import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('Casos_Diarios_Estado_Nacional_Confirmados_20210805.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        y.append(row[1])
        x.append(int(row[3]))

plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Weather Data")

plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Temperature(°C)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()