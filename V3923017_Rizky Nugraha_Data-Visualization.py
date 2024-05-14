#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# printing the top 10 rows
display(data.head(10))


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# Scatter plot w day against tip
plt.scatter(data['Category'], data['Quantity'])

# Adding Title to the plot
plt.title("Test")

# Setting the X and Y labels
plt.xlabel('Category')
plt.ylabel('Quantity')

# Save the plot as a PNG file
plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')

plt.show()


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# Scatter plot w day against tip
plt.plot(data['Category'])
plt.plot(data['Quantity'])


# Adding Title to the plot
plt.title("Test")

# Setting the X and Y labels
plt.xlabel('Category')
plt.ylabel('Quantity')

# Save the plot as a PNG file
plt.savefig('line.png', dpi=300, bbox_inches='tight')

plt.show()


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# Scatter plot w day against tip
plt.bar(data['Category'], data['Quantity'])

# Adding Title to the plot
plt.title("Test")

# Setting the X and Y labels
plt.xlabel('Category')
plt.ylabel('Quantity')

# Save the plot as a PNG file
plt.savefig('bar.png', dpi=300, bbox_inches='tight')

plt.show()


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# Scatter plot w day against tip
plt.hist(data['Category'])


# Adding Title to the plot
plt.title("Histogram")

# Save the plot as a PNG file
plt.savefig('histogram.png', dpi=300, bbox_inches='tight')

plt.show()


# In[14]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("Data Sales3.csv", delimiter = ";")

# Scatter plot w day against tip
sales = ['Category', 'Quantity']
datasales = [23, 10]

plt.pie(datasales, labels=sales)

plt.title("Sales Data")

# Save the plot as a PNG file
plt.savefig('pie.png', dpi=300, bbox_inches='tight')

plt.show()


# In[ ]:




