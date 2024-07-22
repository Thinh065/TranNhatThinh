import pandas as pd
import matplotlib.pyplot as plt
# df = pd.DataFrame({"lab":["A","B","C"],"val":[10,30,20]})
# ax = df.plot.bar(x = "lab",y = "val", rot = 0)
# plt.show()
# -------------

# speed = [0.1, 17.5 , 40 ,48 , 52 , 69, 88]
# lifespan = [2 ,8 ,70 , 1.5 ,25 ,12 ,28]
# index = ["snail", "pig", "elephant", "rabbit","giraffe","coyote","horse"]
# df = pd.DataFrame({"speed":speed,"lifespan": lifespan}, index = index)
# ax = df.plot.bar(rot = 0)
# plt.show()

# cach2
# import matplotlib.pyplot as plt; plt.rcdefaults()
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt 
# objects = ("Python","C++","Java","Perl","Scala","Lisp")
# y_pos = np.arange(len(objects))
# performance = [10,8,6,3,2,1]
# plt.bar(y_pos,performance,align = "center", alpha = 0.5)
# plt.xticks(y_pos,objects)
# plt.ylabel("Usage")
# plt.title("Programming language usage")
# plt.show()

# -----------

import numpy as np
import matplotlib.pyplot as plt
# data to plot 
n_groups = 4
means_frank = (90, 55, 40, 65) 
means_guido = (85, 62, 54, 20)
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups) 
bar_width = 0.35
opacity = 0.8
rects1 = plt.bar (index, means_frank, bar_width,
alpha= opacity,
color='b',
label='Frank')

rects2 = plt.bar (index+bar_width, means_guido, bar_width,
alpha=opacity,
color='g',
label='Guido')

plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D')) 
plt.legend()

plt.tight_layout() 
plt.show()