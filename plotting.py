import matplotlib.pyplot as plt

x=[10,20,30,40]
y=[20,25,35,55]

plt.plot(x,y,color='green',linewidth=3,marker='o',markersize=15,linestyle='--')
plt.title("Customizing Line Chart")
plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.show()

x=['Thur','Fri','Sat','Sun']
y=[170,120,250,190]

plt.bar(x,y,color='green',edgecolor='black',linewidth=2)
plt.title("Bar Chart")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()


