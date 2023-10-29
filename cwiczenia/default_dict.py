# Enter your code here. Read input from STDIN. Print output to STDOUTimport random
from collections import defaultdict

def generate_group(number:int)->list[str]:
    group_str = []
    for index in range(0,int(number)):
        word = input()
        if len(word)>=1 and len(word)<=100:
            group_str.append(word)
    return group_str

def calculate(n_group,m_group):
    d1 = defaultdict(list)
    for index_m,value_m in enumerate(n_group):
        for index_n,value_n in enumerate(m_group):
            if value_m == value_n:
                d1[value_m].append(index_n+1)
    for item in n_group:
        if item not in d1.keys():
            d1[item].append(-1)            
    return d1

n,m=input().split()

m_group = generate_group(number=n)
n_group = generate_group(number=m)
result = calculate(n_group,m_group)
for key,values in result.items():
    print(' '.join(str(e) for e in values))