import matplotlib.pyplot as plt
x = ['kelas a', 'kelas b', 'kelas c', 'kelas d']
y= [30, 35, 49, 25]
plt.pie(y, labels=x, autopct='%.1f%%')
plt.title('diagram lingkaran')
plt.savefig('diagramlingkaran.png')
plt.show()