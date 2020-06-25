# #######################################
# The greater-than symbol followed by space (> ) represents the user input. 
# Notice that it's not the part of the input.
#
# Example 1: a dialogue with the bot
#
# Hello! My name is Aid.
# I was created in 2020.
# Please, remind me your name.
# > Max 
# What a great name you have, Max!
#
##########################################

print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

your_name = input() # reading a name

print('What a great name you have,' + your_name + '!')
