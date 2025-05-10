#subscripting
# print('Hello'[4])


# print(123+456)
# print(123.4 + 5.4)
# print(123.4 + 5)
# print(False)



# num_char = len(input("What's your name?"))


# num= input("Enter a number.")
# convert= str(num)
# print("Your number is " + convert)
# print(type(convert))



# twoDigitNum= input("Type a two digit number.")
# firstNum= twoDigitNum[0]
# secondNum= twoDigitNum[1]
# #type conversion 
# print(int(firstNum) * int(secondNum))
# print(float(firstNum) / float(secondNum))
# print(int(firstNum) + int(secondNum))
# print(int(firstNum) - int(secondNum))
# print(int(firstNum) % int(secondNum))
# print(int(firstNum) ** int(secondNum))



# if  3%3==0:
#     print("Hurray!!!!")
# elif 3-3==1:
#     print("Im an idiot")
# else:
#     print("I am a genius")


import random
# user = input("Type 0 for rock, 1 for paper, 3 for scissors")
# randomNumber = random.randint(1,10)

# print(randomNumber)
# print(round(100* random.random()))

import random

# 1. random() – Random float between 0.0 and 1.0
# print("random():", random.random())

# # 2. uniform(a, b) – Random float between a and b
# print("uniform(10, 20):", random.uniform(10, 20))

# # 3. randint(a, b) – Random integer between a and b (inclusive)
# print("randint(1, 10):", random.randint(1, 10))

# # 4. randrange(start, stop[, step]) – Random number from range
# print("randrange(0, 10, 2):", random.randrange(0, 10, 2))

# # 5. choice(seq) – Random element from a sequence
# print("choice(['apple', 'banana', 'cherry']):", random.choice(['apple', 'banana', 'cherry']))

# # 6. choices(population, weights=None, *, cum_weights=None, k=1) – Random list with replacement
# print("choices(['red', 'green', 'blue'], k=2):", random.choices(['red', 'green', 'blue'], k=2))

# # 7. sample(population, k) – Random list without replacement
# print("sample(range(100), 5):", random.sample(range(100), 5))

# # 8. shuffle(x) – Shuffle list in-place
# lst = [1, 2, 3, 4, 5]
# random.shuffle(lst)
# print("shuffle([1, 2, 3, 4, 5]):", lst)
# print(random.choice(lst))

# # 9. seed(a=None, version=2) – Set seed for reproducibility
# random.seed(42)
# print("Seeded random():", random.random())




# fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# # Without seed: different results every time
# print("No seed, choice():", random.choice(fruits))

# # With seed: same result every time
# random.seed(1)
# print("Seed 1, choice():", random.choice(fruits))

# random.seed(1)
# print("Seed 1, choice() again:", random.choice(fruits))  # Same result as above



# fruits = [ 'apple', 'banana', 'cherry', 'date', 'elderberry', 1, 3.4] #list
# fruits.append('fig') #add to the end
# fruits.insert(2, 'grape') #add to the index
# fruits.remove('banana') #remove
# print(fruits[6])
# fruits[6] = 'kiwi' #replace
# print(fruits[6])

# print(len(fruits)) #length


