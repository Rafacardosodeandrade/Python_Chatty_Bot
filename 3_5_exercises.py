####################################################################################
# N squirrels found K nuts and decided to divide them equally. 
# Determine how many nuts each squirrel will get.
#
# Input data format
#
# There are two positive numbers N and K, each of them is not greater than 10000.
#
# Sample Input 1:
#
# 3
# 14
# Sample Output 1:
#
# 4
#####################################################################################

N = int(input())
K = int(input())
print(K // N)  # put your python code here

#####################################################################
# Given a three-digit integer (i.e. an integer from 100 to 999).
# Find the sum of its digits.
#
# Sample Input 1:
#
# 476
# Sample Output 1:
#
# 17
##############################################################

n = int(input())
a = (n // 100)
b = (n // 10) % 10
c = n % 10
sum_digit = a + b + c
print(sum_digit)


# Write a program that will help people who are going on vacation. The program should calculate the total required sum (e.g. $) of money to have a good rest for a given duration.
#
# There are four parameters which have to be considered:
#
# duration in days
# total food cost per a day
# one-way flight cost
# cost of one night in a hotel (the number of nights equal duration minus one)
# Read integer values of these parameters from the standard input and then print the result.
#
# Hint: Do not forget to consider the flight back
####################################################################################

day = int(input())
food = int(input())
flight = int(input())
night = int(input())
print((day * (food + night)) + (2 * flight) - (night))  # 6 nights and 7 days

# Lucky tickets are a kind of mathematical entertainment. 
# A ticket is considered lucky if the sum of the first 3 digits coincides with 
# the sum of the last 3 digits of the ticket number.
# You are supposed to write a program that checks whether the two sums are equal.
# The code snippet below displays "Lucky" if they do and "Ordinary" otherwise.
#
# However, some parts of the code are missing. Fill in the blanks to make it work!
#
# Input: a string of 6 digits.
#
# Output: either "Lucky" or "Ordinary" (without quotes).
# Hint: Make sure that you are NOT concatenating strings.
# To do this, convert each digit in the ticket number to an integer.
#
#PARAMETERS
# Sample Input 1: 090234
# Sample Output 1: Lucky
#
# Sample Input 2: 123456
# Sample Output 2: Ordinary
####################################################################
# SOLUTION
# Save the input in this variable
ticket = input()

# Add up the digits for each half
half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
half2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")

##################################################################
# For the given amount of money, calculate the income from this
# savings account with a 5% interest rate after one year.
#
# Save the result into the variable income.
#
# SOLUTION:
amount = 1000
interest_rate = 5
years = 1
# change the next line
income = amount * interest_rate / 100
