'''
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
'''

def patter(dimension):
    for row in range(dimension):
        for column in range(row + 1):
            print("* ", end=" ")
        print()

patter(5)