import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline
df = pd.read_csv("vggsound.csv")
# df.groupby('people marching').size().plot(kind='pie', autopct='%.2f')
sns.catplot(x="1", y="test", data=df)
df.groupby('people marching').size().plot(kind='pie', autopct='%.2f')
plt.show()
