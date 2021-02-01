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

''' 8.3 Magic Index ''' 


if __name__ == "__main__":
    pass