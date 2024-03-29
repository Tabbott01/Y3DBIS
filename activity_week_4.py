# -*- coding: utf-8 -*-
"""Activity Week 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b8wD95wAquvIX7g4hDrBu0a6H_X1OiCj

Class Identification Exercise:

Create a vector named animals containing the names of three different animals.
Use the class() function to identify the class of animals.
What class do animals belong to?
"""

animals <- c("fox", "badger", "rabbit")
print(class(animals))

[1] "character"

"""
Define two vectors: numbers1 with the numbers 1 to 3 and numbers2 with the numbers 4 to 6.
Use the c() function to combine the two vectors into a single vector named all_numbers.
Print all_numbers to verify the combination.
"""

numbers1 <- 1:3
numbers2 <- 4:6
all_numbers <- c(numbers1, numbers2)
print(all_numbers)

[1] 1 2 3 4 5 6

"""
Create a vector called temperatures containing the temperatures of a location for a week (e.g., 25, 28, 30, 27, 29, 26, 31).
Use the typeof() function to determine the data type of temperatures.
What data type is temperatures?
"""

temperatures <- c(25, 28, 30, 27, 29, 26, 31)
print(typeof(temperatures))

[1] "double"

"""
Suppose two more animals are added to the animals vector: "elephant" and "tiger".
Remove the second animal from the animals vector.
Print the modified animals vector to verify the removal.
"""

more_animals <- c("elephant", "tiger")
animals <- c(animals, more_animals)
animals <- animals[-2]
print(animals)

[1] "fox"      "rabbit"   "elephant" "tiger"
