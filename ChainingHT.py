#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 22:45:41 2018

@author: dianaramirez
"""
##imported a hash library in python.
import hashlib
# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=277102):##354984 277102
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
            
    ##used the MD5 algorithm found in haslib to create my hashfunction
    ##this algorithm returns a key for each word inserted into the table
    ##I used this key, gave it a int value for each character with ord()
    ## and then took this look key and only utilized the first 17 elements 
    def hash2(self,key):
        hash_object = hashlib.md5(key.encode())
        ##hash_object uses hex encoding
        dummy = hash_object.hexdigest()
        new_string=""
        for char in dummy:
            new_string += str(ord(char))
        new_string = int(new_string)
        new_string = new_string **2
        
        new_string = int(str(new_string)[:21]) ##17
        
        hash_2 = new_string % len(self.table) 
        
        return hash_2
    ##used .sha224 similarly to the hash2 function. Used only the first
    ##  elements
    def hash3(self,key):
        hash_object = hashlib.sha224(key.encode())
        ##hash_object uses hex encoding
        dummy = hash_object.hexdigest()
        new_string=""
        for char in dummy:
            new_string += str(ord(char))
        new_string = int(new_string) **4
        
        new_string = int(str(new_string)[:21])
        hash_3 = new_string % len(self.table)
        return hash_3
    # Inserts a new item into the hashtable.
    def insert(self, item):
        # get the bucket list where this item will go.
        ##bucket = hash(item) % len(self.table)
        ##bucket = self.hash2(item) 
        bucket = self.hash3(item) 
            
        bucket_list = self.table[bucket]
        # insert the item to the end of the bucket list.
        bucket_list.append(item)
         
    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        ##bucket = self.hash2(key) 
        bucket = self.hash3(key) 
        ##bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
       
        # search for the key in the bucket list
        if key in bucket_list:
            # find the item's index and return it 
            return bucket ##bucket_list[item_index]
        else:
            # the key is not found.
            return None

  
    # Overloaded string conversion method to create a string
    # representation of the entire hash table. Each bucket is shown
    # as a pointer to a list object.
    def __str__(self):
        index = 0
        s =  "   --------\n"
        for bucket in self.table:
            s += "%2d:|   ---|-->%s\n" % (index, bucket)
            index += 1
        s += "   --------"
        return s
    
    def longestList(self):
        num_elements = 0
        maxLength = 0
        for i in range(len(self.table)):
            temp = self.table[i]
            num_elements = 0
            for temp in self.table[i]: 
                num_elements +=1
                if maxLength < num_elements:
                    index = i
                    maxLength = max(maxLength,num_elements)
        return maxLength , index
    
    def get_load_factor(self):
        num_elements = 0
        for i in range(len(self.table)):
            temp = self.table[i]
            for temp in self.table[i]:
                num_elements +=1
        return num_elements / len(self.table)
    
    def wasted_space(self):
        ##method to count the number of empty lines left in the table
        wasted_lines = 0
        for i in range(len(self.table)):
            if not self.table[i]:
                wasted_lines +=1
    
        return wasted_lines
    
    def average_length(self):
        ##I used the longestList method to create an array to store the
        ##number of lines with length 0 to length maxl
        
        maxl,index = self.longestList()
        maxl = maxl+1
        lengths = [0]*maxl
        ##counting the number of lines with length 0 to maxl
        for i in range(len(self.table)):
            temp = self.table[i]
            num_elements = 0
            for temp in self.table[i]:
                num_elements +=1   
            i = lengths[num_elements]
            lengths[num_elements] = i+1
        return lengths
    
    def average_search(self):
        lengths = self.average_length()
        average = 0
        for i in range(1,len(lengths)):
            temp = i +.5
            average += (lengths[i]*(temp))
            
        average = average // len(self.table)
        return average