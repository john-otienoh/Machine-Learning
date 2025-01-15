import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)
# Sine wave
plt.plot(x, y, 'g*')
plt.plot(x, z, 'r+')
plt.xlabel("Angle")
plt.ylabel("Sine/Cosine")
plt.title("SIne/Cosine Wave")
# plt.show()

# Bar Plot
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
languages = ['Eng', 'Fre', 'Ger', 'Lat']
people  = [100, 39, 123, 34]
ax.bar(languages, people)
plt.xlabel("Languages")
plt.ylabel("number of People")
# plt.show()

# Pie Chart
ax.pie(people, labels=languages, autopct='%1.1f%%')
plt.show()
