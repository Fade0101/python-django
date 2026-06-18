import math
from random import random


l1 =[1,1,2,3,3,4] 
def remove_duplicates(l):
    return list(set(l))
print(remove_duplicates(l1))

def front_back_merge(a: str, b: str) -> str:
    split_a = (len(a) + 1) // 2 
    split_b = (len(b) + 1) // 2
    a_front, a_back = a[:split_a], a[split_a:]
    b_front, b_back = b[:split_b], b[split_b:]
    return a_front + b_front + a_back + b_back



print(front_back_merge("abcd", "xy"))    
print(front_back_merge("abcde", "xyz"))  

def is_set(list):
    if len(list) == len(set(list)):
        return True
    else:
        return False
    
print(is_set([1,2,3]))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 1,25, 12, 90]
print(bubble_sort(arr)) 
import random

def guessing_game():
    while True:
        tries = 10
        secret_number = random.randint(1, 100)
        guessed_numbers = []

        print("\nA new number has been generated!")

        while tries > 0:
            user_guess = int(input("Enter your guess (1-100): "))
         

            if user_guess < 1 or user_guess > 100:
                print("Number out of range! This try will not be counted.")
                continue

            if user_guess in guessed_numbers:
                print("You already entered this number! This try will not be counted.")
                continue

            guessed_numbers.append(user_guess)
            tries -= 1

            if user_guess == secret_number:
                print("Congratulations You guessed correctly!")
                print(f"Remaining tries: {tries}")

                secret_number = random.randint(1, 100)
                guessed_numbers.clear()

                if tries == 0:
                    break

                print("\nA new number has been generated!")
                continue

            elif user_guess < secret_number:
                print("Too low!")

            else:
                print("Too high!")

            print(f"Remaining tries: {tries}")

        print("\nGame Over!")

        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again != "y":
            print("Thanks for playing")
            break


guessing_game()
