"""
a = input("Enter a filename")
s ={}
with open(a,"r") as f:
    for i in f.readlines():
        for j in i.split():
            if j in s.keys():
                s[j] += 1
            else:
                s[j] = 1
sortedWordFreq = sorted(s.items(), key=lambda x:x[1], reverse=True )
print("===================================================")
print("10 most frequently appearing words with their count")
print("===================================================")
for i in range(10):
    print(sortedWordFreq[i][0], "occurs", sortedWordFreq[i][1], "times")
"""


"""
a = "test.txt" #input("Enter a filename")
s =[]
with open(a,"r") as f:
    for i in f.readlines():
        s.append(i.strip())
s.sort()
with open("newfile.txt","w") as p:
    for i in s:
        p.write(i +"\n")
with open("newfile.txt","r") as p:
    for i in p.readlines():
        print(i.strip())
"""
from zipfile import ZipFile
import os , sys , pathlib
a =  input("Enter a file name to zip")

if not os.path.isdir(a):
    pass