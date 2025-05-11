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


# numbers= [1,2,3,4,5,6,7,8,9]

# for number in numbers:
#     print(number)
# for number in range(2,101,2):
#     print(number)

# letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# symbols= ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']


# print("Welcome to the password generator.")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_numbers = int(input("How many numbers would you like?\n"))
# password= ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)    
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)


# def add(n1, n2):
#     return n1 + n2


# while True:
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         result = add(num1, num2)
#         print(f"The sum is: {result}")
#         break
#     except ValueError:
#         print("Invalid input. Please enter numbers only.")



# words= ["hello", "world", "python", "programming", "language", "code", "computer", "science", "artificial", "intelligence"]
# random_word = random.choice(words)
# blank_word = ['_' for _ in random_word]
# tries=5
# while True:
#     guess = input(f"Guess a letter in the word {blank_word}: ").lower()
#     if len(guess) != 1 or not guess.isalpha():
#         print("Please enter a single letter.")
#         continue
#     if guess in random_word:
#         blank_word = "".join([random_word[i] if random_word[i] == guess else blank_word[i] for i in range(len(random_word))])
#         print(f"Good guess! The word now looks like this: {blank_word}")
#     else:
#         print("Sorry, that letter is not in the word.")
#     if "_" not in blank_word:
#         print(f"Congratulations! You've guessed the word: {random_word}")
#         break
# print("Game Over")
# print("The word was:", random_word)


# while True:
#     guess = input("Guess a letter in the word: ").lower()
#     if len(guess) != 1 or not guess.isalpha():
#         print("Please enter a single letter.")
#         continue
#     if guess in random_word:
#         for i, letter in enumerate(random_word):
#             if letter == guess:
#                 blank_word[i] = guess
#         print(f"You guessed a correct letter. Here's how it looks: {' '.join(blank_word)}")
#     else:
#         tries-=1
#         print("You entered a wrong letter. No of tries left: ", tries )
#         if tries == 0:
#             print("Game Over")
#             print("The word was:", random_word)
#             break
#     if "_" not in blank_word:
#         print(f"Congratulations! You've guessed the word: {random_word}")
#         break

# def noOfCans(height, width):
#     area = height * width
#     canArea = 5
#     noOfCans = area / canArea
#     return noOfCans

# height = int(input("Enter the height of the wall: "))
# width = int(input("Enter the width of the wall: "))
# noOfCans = noOfCans(height, width)
# print(f"You will need {noOfCans} cans of paint to cover the wall.")


#Caesar Cipher
# alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
# text=input("Type your message:\n").lower()
# shift= int(input("Type the shift number:\n"))

# def encrypt(text, shift):
#     cipherText=""
#     for letter in text:
#         position = alphabet.index(letter)
#         newPosition = position + shift
#         newLetter = alphabet[newPosition]
#         cipherText+= newLetter
#     print(f"The encoded text is: {cipherText}")
# encrypt(text, shift)

#Dictionaries
# dictionary = {
#     "a": "apple",
#     "b": "banana",
#     "c": "cherry",
#     "d": "date",
#     "e": "elderberry",
#     "f": "fig",
#     "g": "grape",
#     "h": "honeydew",
#     "i": "kiwi",
#     "j": "jackfruit",
#     "k": "kiwi",
#     "l": "lemon",
#     "m": "mango",
#     "n": "nectarine",
#     "o": "orange",
#     "p": "papaya",
#     1: "one",
# }
# print(dictionary[1]) 
# dictionary[1] = "two"
# dictionary[2] = "two"
# print(dictionary[1])
# print(dictionary[2])


# for thing in dictionary:
#     print(thing)
#     print(dictionary[thing])


# studentScores= {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }
# studentGrades = {}
# for student in studentScores:
#     score = studentScores[student]
#     if score >= 91:
#         studentGrades[student] = "Outstanding"
#     elif score >= 81:
#         studentGrades[student] = "Exceeds Expectations"
#     elif score >= 71:
#         studentGrades[student] = "Acceptable"
#     else:
#         studentGrades[student] = "Fail"


# print(studentGrades)


#Nesting
#Dictionaries inside a list
# courses=[
#     {
#         "semester": "1",
#         "programmingLanguage": "c",
#     },
#     {
#         "semester": "2",
#         "programmingLanguage": "java",
#     },
#     {
#         "semester": "3",
#         "programmingLanguage": "java",
#     },
#     {
#         "semester": "4",
#         "programmingLanguage": "c++",
#     },
#     {
#         "semester": "5",
#         "programmingLanguage": "javascript",
#     },
#     {
#         "semester": "6",
#         "programmingLanguage": "python",
#     },
#     {
#         "semester": "7",
#         "programmingLanguage": "c sharp",
#     }         
# ]

# print(courses[0])
# print("Welcome to the sceret auction program.")
# bids={}
# while True:
#     name = input("What is your name? ")
#     price = int(input("What is your bid? $"))
#     bids[name] = price
#     more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
#     if more_bids == "no":
#         break
    
# def find_highest_bidder(bidding_record):
#     highest_bid=0
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}.")
# find_highest_bidder(bids)


# #BlackJack
# from random import shuffle
# cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
# def deal_card():
#     return cards[random.randint(0, 12)]
# def calculate_score(hand):



#Scope
# enemies=1
# def increase_enemies():
#     enemies=2 #inorder to access the global variable, we need to use the global keyword 
    
#     print(f"Enemies inside function: {enemies}")
# increase_enemies()
# print(f"Enemies outside function: {enemies}")
    
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
# number = random.randint(0,100)
# print(f"Your number is {number}")
# attempts = 0
# if difficulty == "easy":
#     attempts = 10
# else:
#     attempts = 5
# while attempts !=0:
#     print(f"You have {attempts} attempts remaining to guess the number.")
#     guess = int(input("Make a guess: "))
#     if guess == number:
#         print(f"You got it! The answer was {number}.")
#         break
#     elif guess < number:
#         attempts -= 1
#         print("Too low. Attempts left: ", attempts)
#     elif guess > number:
#         attempts -= 1
#         print("Too high. Attempts left: ", attempts)
#     if attempts == 0:
#         print(f"You lost. The number was {number}.")
