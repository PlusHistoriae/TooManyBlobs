import matplotlib.pyplot as plt
import random as rdm
import numpy as np

      #VARTIABLRES

days = 100

species_population = 35
predator_population = 60
tree_population = 120

trees = np.arange(tree_population)
predators = np.arange(predator_population)
species = np.arange(species_population)

predator_assignment = rdm.sample(list(trees), predator_population)

species_data = []
predator_data = []
tree_data = []

      #CODE

print(predator_assignment)
for simulation in range(days):
  # assign species members to trees
  species_assignment = rdm.sample(list(trees), species_population)

  # remove species memebers that interact with predators
  for i in range(species_population):
    if species_assignment[i] in set(predator_assignment):
      species_population = int(species_population - 1)

  # species members that survived reproduce

  for reproduce in range(species_population):
    species_population = species_population + rdm.randint(0,2)

  if species_population >= tree_population:
    species_population = 5

  # appending data to graph
  
  species_data.append(species_population)
  predator_data.append(predator_population)     
  tree_data.append(tree_population)
  print(species_population)

# creating graph

Title = input("What is the name of the Graph?      ")

plt.plot(species_data, label = "Species")
plt.plot(predator_data, label = "Predator")
plt.plot(tree_data, label = "Trees")

plt.title(Title)
plt.legend()
plt.xlabel('Time')
plt.ylabel('Population')

plt.show()