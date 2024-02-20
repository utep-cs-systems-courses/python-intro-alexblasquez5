#! /usr/bin/env python3

import re
import sys

def count(input_file, output_file):
    #Reads file
    with open(input_file, 'r') as file:
        text = file.read().lower()

    #Finds all the words in the file
    words = re.findall(r'\b\w+\b', text)

    #Count occurrances
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    #Sort to alphabetical order
    sorted_word_count = sorted(word_count.items())

    #Write output file
    with open(output_file, 'w') as file:
        for word, count in sorted_word_count:
            file.write(f"{word} {count}\n")

        
