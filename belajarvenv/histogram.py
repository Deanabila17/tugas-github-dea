import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(100,300,400)
plt.hist(x)
plt.title('histogram')
plt.savefig('histogram.png')
plt.show()