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