from io import open
import glob
import os
import unicodedata
import string
import os


def findFiles(path): return glob.glob(path)

# Turn a Unicode string to plain ASCII
def unicodeToAscii(s):
    all_letters = string.ascii_letters + " .,;'-"
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )

# Read a file and split into lines
def readLines(filename):
    lines = open(filename, encoding='utf-8').read().strip().split('\n')
    return [unicodeToAscii(line) for line in lines]



def load_data (path):
    # Build the category_lines dictionary, a list of lines per category
    category_lines = {}
    all_categories = []
    for filename in findFiles(os.path.join(path,'*.txt')):
        category = os.path.splitext(os.path.basename(filename))[0]
        all_categories.append(category)
        lines = readLines(filename)
        category_lines[category] = lines

    n_categories = len(all_categories)

    print('# categories:', n_categories, all_categories)
    print("transformed French Name O'Néàl:",unicodeToAscii("O'Néàl"))
    return category_lines , all_categories, n_categories