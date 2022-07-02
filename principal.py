import matplotlib.pyplot as plt
print("ingrese el nùmero de puntos a graficar\n")
n=int(input("n= "))

for m in range(n+1):#m comienza en 0 y toma valores hasta n 
   plt.plot(m,m**0.5,marker ="o")
#m=m+1

plt.grid()
plt.show()

