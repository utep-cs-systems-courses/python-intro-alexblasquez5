import re
import sys
import os

def count(input_file, output_file):
    inputF = os.open(input_file, os.O_RDWR)
    size = os.stat(inputF).st_size
    read = os.read(inputF, size)
    os.close(inputF)
    
    #Turn file from bytes to words
    text = read.decode('utf-8')
    
    #Reads all words in the file
    words = re.findall(r'\b\w+\b', text.lower())

    #Count number of types each word appears
    word_dic = {}

    current_word = ''
    for string in text:
        if not check_char(string) and (string.isspace() or string == '-' or string == "'"):
            if current_word:
                current_word = current_word.strip()
                word_dic[current_word] = word_dic.get(current_word, 0) + 1
                current_word = ''
            else:
                current_word += string.lower()

    #Sort the dictionary
    sorted_dic = {key: word_dic[key] for key in sorted(word_dic.keys())}

    #Write the dictionary in the output file
    outputF = os.open(output_file, os.O_RDWR | os.O_CREAT)
    for key, value in sorted_dic.items():
        byte_type = (f"{key} {value}\n").encode('utf-8')
        os.write(outputF, byte_type)


    os.close(outputF)
                                      
def check_char(i):
    punctuation = {",", ".", ":", ";"}
    if i in punctuation:
        return True
    else:
        return False


inputTo = sys.argv[1]
outputTo = sys.argv[2]

count(inputTo, outputTo)
