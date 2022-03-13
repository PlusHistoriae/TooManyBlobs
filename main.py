      #PACKAGES/MODULES

import matplotlib.pyplot as plt
import random as rdm

      #VARTIABLRES

species_data = []
predator_data = []
tree_data = []

days = int(input("How many days should the simulation run for?     "))
print()
species_population = int(input("How many of the species would you like?    "))
print()
predator_population = int(input("How many of the predators would you like?    "))
print()
tree_population = int(input("How many of the trees would you like?    "))
print()

apples = int(tree_population*2)

      #CODE

for simulation in range(days):
  apples = int(apples - species_population)
  
  apples = int(tree_population*2)

#Plotting the Data on a Graph (uses matplotlib)

species_data.append(species_population)     #Species
plt.plot(species_data, label = "Species")
predator_data.append(predator_population)     #Predators
plt.plot(predator_data, label = "Predator")
tree_data.append(tree_population)     #Trees
plt.plot(tree_data, label = "Trees")

Title = input("What is the name of the Graph?      ")

plt.title(Title)
plt.legend()
plt.xlabel('Time')
plt.ylabel('Population')

plt.show()