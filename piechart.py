# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# df = pd.DataFrame({"mass": [0.330, 4.87,5.97],
#                    "radius": [2439.7,6051.8,6378.1]},
#                    index = ["Mercury","Venus","Earth"])
# plot = df.plot.pie(y = "mass", figsize = (5,5))
# plt.show()

# CACH 2

# import matplotlib.pyplot as plt

# labels = "Python", "C++", "Ruby", "Java"
# sizes = [215, 130, 245, 210]
# colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue"] 
# explode = (0.1, 0, 0, 0) 

# plt.pie(sizes, explode=explode, labels=labels, colors=colors, 
# autopct="%1.1f%%", shadow=True, startangle=140)
# plt.axis("equal") 
# plt.show()

# 

import matplotlib.pyplot as plt
labels = ["Cookies", "Jellybean", "Milkshake", "Cheesecake"]
sizes = [38.4, 40.6, 20.7, 10.3]
colors = ["yellowgreen", "gold", "lightskyblue", "lightcoral"]
patches, texts = plt.pie (sizes, colors=colors, shadow=True, startangle=90)
plt.legend (patches, labels, loc= "best")
plt.axis("equal")
plt.tight_layout() 
plt.show()