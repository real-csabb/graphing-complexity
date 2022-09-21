import random

def generate_array(n):
  # Initialize array
  arr = []

  # Iterate through array generating randint between min and max
  for i in range(n):
    arr.append(random.randint(0, 1000000))

  return arr