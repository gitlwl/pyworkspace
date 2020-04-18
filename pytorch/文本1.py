from __future__ import unicode_literals,print_function,division
from io import open
import glob
import os
import torch

def findFiles(path):return glob.glob(path)
print(findFiles('data/names/*.txt'))
import unicodedata
import string
all_letters=string.ascii_letters+" .,;'"
n_letters=len(all_letters)
def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD',s)
        if unicodedata.category(c) !='Mn'
        and c in all_letters
    )
print(unicodeToAscii('Slusarski'))
category_lines={}
all_categories=[]
def readLines(filename):
    lines=open(filename,encoding='utf-8').read().strip().split('\n')
    return [unicodeToAscii(line) for line in lines]
for filename in findFiles('data/names/*.txt'):
    category= os.path.splitext(os.path.basename(filename))[0]
    all_categories.append(category)
    lines=readLines(filename)
    category_lines[category]=lines
n_categories=len(all_categories)
print(category_lines['Italian'][:5])
#将姓氏转化为张量

def letterToIndex(letter):
    return all_letters.find(letter)
def letterToTensor(letter):
    tensor=torch.zeros(1,n_letters)
    tensor[0][letterToIndex(letter)]=1
    return tensor
def lineToTensor(line):
    tensor=torch.zeros(len(line),1,n_letters)
    for li,letter in enumerate(line):
        tensor[li][0][letterToIndex(letter)]=1
    return tensor
print(letterToIndex('J'))
print(lineToTensor('Jones').size())
#创建网络


