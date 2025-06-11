#!/usr/bin/env python3

def happy_new_year():
    i = 0
    while i < 11:
        print(f'{i}')
        i += 1
        print("Happy New Year!")

def square_integers(int_list):
    new_nums = list()
    for i in int_list:
        new_num = i ** 2
        new_nums.append(new_num)
    return new_nums
        

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print(i)