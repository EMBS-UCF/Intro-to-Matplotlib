#Sonny Maiorino
#11/10/26
#EMBS 2026 - Fall Workshop #3
#Intro to Matplotlib

#declare libraries to use
import matplotlib.pyplot as plt
import pandas as pd

#read data (add YOUR OWN dataset)
data_file = "Basic-SampleDataset.xlsx" #run this script from the code folder, or point this at your own file
df = pd.read_excel(data_file) #set up DataFrame, which is how data transformed into graph

#set axes and labels
x = df['Time (ms)']
y = df['Distance (um)']
c = df['Hydrodynamic Radius (nm)']
plt.grid()
#ax = plt.axes() #(background) set BEFORE plotting!
#ax.set_facecolor('silver')
#plt.plot(x,y) #NEED a command like this to get things on axes     
plt.scatter(x,y) #what if you changed to "scatter" instead? (start of 2)                                                                                                             
#plt.scatter(x,y,c=c,s=20) #(hue) c = color, s = size
#plt.scatter(x,y,marker='x') #(marker shape) 'o' for O, 'x' for X, '*' for star, 's' for square, 'D' for diamond, etc.
#plt.scatter(x,y,marker='x') #(marker shape) 'o' for O, 'x' for X, '*' for star, 's' for square, 'D' for diamond, etc.
plt.axline((0,0), (20,0), color='k') #draws black x-axis
plt.xlabel("Time (ms)", fontname = "Times New Roman", fontsize = 14)
plt.ylabel("Distance (um)", fontname = "Times New Roman", fontsize = 14)
plt.title("Distance of Protein Motion", fontname = "Times New Roman", fontsize = 18)

#color your graph (preferably disability-friendly)
plt.style.use("seaborn-v0_8-notebook") #colorblind-friendly style
#plt.grid() #(grid)

#present at the end
plt.legend() #(not needed here)
plt.show()