#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 22:46:49 2018

@author: Diana Ramirez 88604827
CS3 Lab 4B
Professor D. Aguirre
1:30PM 
"""
from ChainingHT import ChainingHashTable

g = open("wordsO.txt")
word_list = g.readlines()

hashChain = ChainingHashTable()

##populating the hash table from the word list
for ln in word_list:
    ln = ln.replace('\n','')
    hashChain.insert(ln)
    
print(hashChain)

word = input("Which key would you like to search for? ")
print("Item found in key: ",hashChain.search(word))
length,index = hashChain.longestList()
print("The longest list in my hash table is",length,"items long, at index",index)

print(f'My load factor was {hashChain.get_load_factor():.2f}')##.format(hashChain.get_load_factor()))
print("Num of empty lines", hashChain.wasted_space())
##shows the number of indexes with lenghts 0 to longestList size
print("Array lists lengths", hashChain.average_length())
##I used a histogram sort of approach to find the average comparisons 
##the search method does when searching for any word in the hash table
print(f'Average search comparisons is about {hashChain.average_search():.2f}')
