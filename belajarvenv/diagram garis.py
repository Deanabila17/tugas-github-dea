import matplotlib.pyplot as plt
x = [2, 4, 6, 7, 8,]
y= [2, 7, 9, 10, 1]
plt.plot(x,y, marker='*')
plt.title('diagram garis')
plt.savefig('diagramGaris.png')
plt.show()