'''
implement an NxN jigsaw puzzle

design the data structures and explain an algorithm to solve the puzzle.
you can assume you have a fitsWith(edge1, edge2) method which,
    when passed 2 puzzle edges, returns True if the 2 edges belong together
'''
class FullPuzzle():
    pass

class Piece():
    '''
    Structures:
        4 strings (LEFT, RIGHT, TOP, BOTTOM) representing side type
            OUTER, INNER, or FLAT
        Point location (x,y) representing location on puzzle
    Methods:
        see_available_count()
        accept_vechicle(vechicle)
    '''