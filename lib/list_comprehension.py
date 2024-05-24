#!/usr/bin/env python3

def return_evens(num_list):
    # even_num_list = []
    # for i in num_list:
    #     if i % 2 == 0:
    #         even_num_list.append(i)

    # return even_num_list
    even_num_list = [i for i in num_list if i % 2 == 0]
    return even_num_list

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]


print(return_evens([0, 1, 3, 5, 7, 8, 9]))
# [0, 8]
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
# ["Hello!", "I'm doing great!", "Python is fun!"]