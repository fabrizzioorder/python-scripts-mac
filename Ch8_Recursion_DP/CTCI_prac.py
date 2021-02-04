'''
Chapter 8: Recursion and Dynamic Programming

Piero Orderique
Started 01 Feb 2021
'''

''' 8.1 Triple Step '''
def count(n):
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4

    a, b, c = 1, 2, 4

    for i in range(4, n):
        nxt = a + b + c
        a = b
        b = c
        c = nxt
    
    return a + b + c

''' 8.2 Robot in Grid '''
grid = [['S', ' ', ' '],
        [' ', ' ', ' '],
        [' ', 'X', ' '],
        [' ', 'X', 'E']]
def move(grid):
    # go down 
    pass

''' 8.4 Power Set ''' 
# fix later. You can't hash a list or set
def powersets(s:set) -> list:
    res = set()
    if len(s) == 0: return set(set())
    if len(s) == 1: set([s, set()])
    
    extra = s.pop() # pop random
    ps = powersets(s) # get rest of power sets
    res.extend(ps)

    for sett in ps:
        sett.add(extra)
        res.append(sett)

    return res

''' 8.5 Recursive Multiply '''
def mul(a, b):
    return multi(a, b, res=0)

def multi(a, b, res=0):
    if b == 0: return res
    res += a
    b -= 1
    return multi(a, b, res)

''' 8.6 Towers of Hanoi '''
def hanoi(start:list , mid:list, end:list, n:int):
    if n == 1: 
        end.append(start.pop())
    else:
        hanoi(start, end, mid, n-1)
        end.append(start.pop())
        hanoi(mid, start, end, n-1)
    
''' 8.7 Permutations w/o Duplicates '''
def perm(s:str):
    res = []
    if len(s) == 1: 
        return [s]

    char = s[-1] # extra char
    s = s[:len(s)-1] # remove that char
    subs = perm(s) # get the sub permutations

    for p in subs:
        for idx in range(len(p)+1):
            res.append(p[:idx] + char + p[idx:])
    
    return res

if __name__ == "__main__":
    print(perm("abc"))