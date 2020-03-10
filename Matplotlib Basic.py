from matplotlib import pyplot as plt
from matplotlib import  style
style.use("ggplot")

x= [5,8,12]
y= [12,16,6]

x1= [6,9,11]
y1= [6,15,17]

plt.plot(x,y,'g',label="line 1", linewidth=5)
plt.plot(x1,y1,'c',label="line 2", linewidth=5)
plt.title("Info")
plt.ylabel("Y-axis")
plt.xlabel("X-Label")
plt.legend()
plt.grid(True,color='K')
plt.show()