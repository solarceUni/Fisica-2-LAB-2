import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.patheffects as path_effects

df = pd.read_csv("hola2.csv", sep=",",header=None)
time = df[0]
pos = df[2]


plt.rcParams['font.family'] = 'Consolas'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 20



fig, ax = plt.subplots()
ax.plot(time,pos, linewidth=3,linestyle='solid',color='red', path_effects=[path_effects.SimpleLineShadow(),
                       path_effects.Normal()])
ax.grid(True, linestyle = '--')
ax.set_title("Grafico Velocidad / Tiempo")
ax.set(xlabel='Tiempo (s)', ylabel="Velocidad (m/s)")

plt.show()