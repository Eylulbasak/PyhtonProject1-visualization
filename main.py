import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset('titanic')
#df['sex'].value_counts().plot(kind='bar')
#plt.show()
plt.hist(df['age'])
plt.show()
plt.boxplot(df['fare'])
plt.show()

#plot ozellikleri

x = np.array([1,10])
y = np.array([0,150])
plt.plot(x,y, 'o')
plt.show()
plt.plot(x,y)
plt.show()


#marker

y = np.array([13,28,17,10])

plt.plot(y, marker='*')
plt.show()

#line

y = np.array([4,9,3,7,15])
plt.plot(y, linestyle='dotted', color='r')
plt.show()
#multiple
x = np.array([1,10,5,8,13,23])
y = np.array([0,15,7,4,22,56])
plt.plot(x)
plt.plot(y)

plt.title('ana baslik')
plt.xlabel('xin basligi')
plt.ylabel('ynin basligi')
plt.grid()
plt.show()

