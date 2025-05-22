import re
from collections import Counter


def count_word(file_path):
    with open(file_path,'r') as file:
        text = file.read().lower()
    words = re.findall(r'\b\w+\b',text)
    
    word_count = Counter(words)
    for word, count in word_count.items():
        print(f'{word}: {count}')
        
file_path = 'words.txt'
count_word(file_path)
