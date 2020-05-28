# # lists
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# # list comprehensions
# first_col=[row[0] for row in matrix]
# print(first_col)
# # sets
# x=set()
# x.add(1)
# x.add(2)
# x.add(2)
# print(x)
# y=set([1,2,3,4,4,5,5,6,6,6,])
# print(y)

# d={'key1':1,'key2':2}
# for items in d:
#     print(items)
#     print(d[items])

# t=[(1,2),(3,4)]
# for t1,t2 in t:
#     print(t1)
#     print(t2)
#
# l=[[1,2],[3,4]]
# for l1,l2 in l:
#     print(l1)
#     print(l2)

# i=1
# while i<5:
#     print('i is: {}'.format(i))
#     i+=1

# a=[1,2,3,4]
# out=[num*2 for num in a]
# print(out)

# mylist=[1,2,3,4,5,6,7,8,9]
# def even_bool(num):
#     return num%2==0
# evens=filter(even_bool,mylist)
# print(list(evens))
# evs=filter(lambda num: num%2==0, mylist)
# print(list(evs))

# print('x' in [1,2,'x'])



# ---------------------------------------------------------------------------------------------------------
# game project
import random

# get guess
def get_guess():
    return list(input('What is your guess?'))

# generate computer code
def generate_code():
    digits=[str(num) for num in range(10)]
    # shuffle the digits
    random.shuffle(digits)
    # then grab the first three
    return digits[:3]



# generate the clues
def generate_clues(code,user_guess):
    if user_guess==code:
        return 'CODE CRACKED'
    clues=[]

    for ind,num in enumerate(user_guess):
        if num==code[ind]:
            clues.append('match')
        elif num in code:
            clues.append('close')
    if clues==[]:
        return ['nope']
    else:
        return clues
# run game logic
print('Welcome Code Breaker!')
secret_code=generate_code() 
clue_report=[]
while clue_report != 'CODE CRACKED!':
    guess=get_guess()
    clue_report=generate_clues(guess,secret_code)
    print('here is your guess:')
    for clue in clue_report:
        print(clue)
