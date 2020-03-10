from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")

x= [1,3,5,7,9]
y= [5,2,7,8,2]

x1= [2,4,6,8,10]
y1= [8,6,2,5,6]

plt.bar(x,y,color='g',label="line 1")
plt.bar(x1,y1 ,label="line 2")
plt.title("Bar Graph")
plt.ylabel("Y-axis")
plt.xlabel("X-axis")
plt.legend()
plt.show()