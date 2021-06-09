import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(1,10,10)
b = np.random.randint(1,10,10)

#Udelej pro 2 sloupce
fig, ax = plt.subplots(figsize = (10,5))
rectss = []
rectss.append(ax.bar(range(len(a)), a, color = [plt.get_cmap('tab20')(i) for i in np.linspace(0,1,len(a)*2)[0::2]], align = 'center'))
rectss.append(ax.bar(range(len(a)), b, color = [plt.get_cmap('tab20')(i) for i in np.linspace(0,1,len(a)*2)[1::2]], align = 'edge'))
for rects in rectss:
    for rect in rects:
        ax.annotate(rect.get_height(), (rect.get_x() + rect.get_width()/2, rect.get_height()), ha = 'center', va = 'bottom') #, color = 'green'
        #rect.set_color('green')
ax.xaxis.grid()
ax.yaxis.grid()
#plt.grid(True)
plt.xticks(range(len(a)), range(len(a)), rotation=45)
plt.xlabel('Ahoj')
plt.title("Dnes", fontweight="bold")
plt.show()
