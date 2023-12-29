import random
import operator
from matplotlib import pyplot as plt

collection =[]
count_dict={}
sample_size=500000
for q in range(sample_size):

    string = ""
    ele = random.randint(0,35)
    if(ele<10):
        string+=str(ele)
    else:
        string+=chr(ele-10+65)

    coin=["Head","Tail"]
    for i in range(2,9):
        if(random.choice(coin) == "Tail"):
            ele = random.randint(0,35)
            if(ele<10):
                string+=str(ele)
            else:
                string+=chr(ele-10+65)

    lowest_base_char=max(string)
    lowest_base = int(ord(lowest_base_char)-65+10)+1 if lowest_base_char.isalpha() else int(lowest_base_char)+1
    collection.append(lowest_base)
    if(count_dict.get(lowest_base)==None):
        count_dict[lowest_base] = 1/sample_size
    else:
        count_dict[lowest_base] += 1/sample_size
plt.bar(x=count_dict.keys(),height=count_dict.values())
plt.show()

