import matplotlib.pyplot as plt
plt.title("Product Sold")
x = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
y = [10,25,50,75,100,150,200]
colors = ["red", "pink", "orange", "yellow", "green", "blue", "purple"]
plt.bar(x,y, color=colors)
plt.xticks(range(len(x)), x)
plt.xlabel("This Week")
plt.ylabel("Products Sold")
plt.show()