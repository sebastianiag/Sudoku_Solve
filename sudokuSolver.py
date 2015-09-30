
class Sudoku:
    
    def __init__(self,puzzle):
        self.puzzle = list(puzzle)  
    
    def solve(self):    
        h = {}
        for j in range(81):
            if self.puzzle[j] != '0':           #If the square already has a value, skip it
                continue
            else:
        
                for k in range(80):
				'''
				This gets the indexes of all squares in the row and column where the current square is located 
				'''
                    if (k/9 == j/9) or (k%9 == j%9) or (k/27 == j/27) and ((k%9)/3 == (j%9)/3): 
                        temp = self.puzzle[k]    
                    else:
                        temp =0   
                    h[temp] = 1    #'temp' is the value inside the k-th square, and shall be stored as a hash key
            for i in range(1,10):
                if str(i) in h:    #eliminates values that are already used in the reference row and column
                    continue
                else:
                    self.puzzle[j] = str(i)
                    self.solve()  #Recursive function call
            self.puzzle[j] = '0'  #If it happens that no value from (1-9) could be found for the current square, assign it zero and start again(backtrack)
            return self.puzzle[j]
            

        print "\n\nThe solution to the problem is:\n"
		'''
		This is the 81x81 square generator
		'''
        print "+" + "-"*29 + "+"

        for x in range(1,82):
            print self.puzzle[x-1],
            if x%3 == 0 and x%9 !=0:
                print "|",
            
            if x%9 == 0 and x%81 !=0:
                print "|\n|"+ "-"*29 + "|\n|",
            if x%81 == 0:
                print "|",

        print "\n+" + "-"*29 + "+"
        return None

#-------------------------------------------------------------------------------
import sys

try:
    puzzle = Sudoku(sys.argv[1])
    print "\nSolving puzzle please wait for a moment\n"
    puzzle.solve()
   
except:
    print "Error => usage of this program is as follows: python sudokuSolver.py <Enter 81 string, put 0 for blanks>"
    sys.exit(0)

