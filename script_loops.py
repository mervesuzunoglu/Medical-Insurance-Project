# Working with Python loops to iterate through and analyze medical insurance cost data

names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]

estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]

actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Avarage insurance cost calculation

total_cost = 0

for costs in actual_insurance_costs:
  total_cost += costs

average_cost = total_cost / len(actual_insurance_costs)
print("Average Insurance Cost: "+ str(average_cost) + " dollars.")

# For each individual in names, calculating whether their insurance cost is above or below average

for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")
  if insurance_cost > average_cost:
    print("The insurance cost for " + name + " is above average.")
  elif insurance_cost < average_cost:
    print("The insurance cost for " + name + " is below average.")
  else:
    print("The insurance cost for " + name + " is equal average.")

# Creating a list comprehension to calculate actual insurance cost

updated_estimated_costs = [estimated_cost * 11/10 for estimated_cost in estimated_insurance_costs]

print(estimated_insurance_costs)
