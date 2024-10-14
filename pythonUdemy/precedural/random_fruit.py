import random

fruits = ['mangue', 'orange', 'banane', 'cerise', 'pomme', 'mandarin', 'peche']
#random_index = random.randint(0, len(fruits) - 1)
random_fruit = random.choice(fruits)
print(random_fruit)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])