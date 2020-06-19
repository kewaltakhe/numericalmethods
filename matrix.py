import numpy as np
import sympy as sp
from fractions import Fraction
import re
from pprint import pprint

class FuzzyMatrix3xN:
    
    def __init__(self, matrix):
        self.matrix=np.array(matrix)
        self.opts=[]
        self.snapshots=[self.matrix.copy()]
        
    def apply_to_matrix(self,opt,revert=False):
        match=re.match(r'\s*r(\d){1}\s*=\s*r(\d){1}\s*([+-]){1}\s*(-?\d*\/?\d*)\s*r(\d){1}\s*$',opt)
        print(opt)
        ra=int(match.group(1))-1
        rb=int(match.group(2))-1
        rc=int(match.group(5))-1
        factor=float(Fraction(match.group(4)))
        sign=match.group(3)
        if sign=='+':
            self.matrix[ra]=self.matrix[rb]+factor*self.matrix[rc]
            if revert==False:
                self.opts.append(opt)
        elif sign=='-':
            self.matrix[ra]=self.matrix[rb]-factor*self.matrix[rc]
            if revert==False:
                self.opts.append(opt)
        if(revert==False):
            self.snapshots.append(self.matrix.copy())
                
    def operate_rows(self):
        print("enter: \nq-menu,\np-print matrix, \nsnaps-print snaps, \nopts-see operations performed, \nr- revert an operation.")
        while True:
            opt=input(">")
            if(re.match(r'\s*r(\d){1}\s*=\s*r(\d){1}\s*([+-]){1}\s*(-?\d*\/?\d*)\s*r(\d){1}\s*$',opt)):
                self.apply_to_matrix(opt)
                print((self.matrix))
            elif(opt=='p'):
                print((self.matrix))
            elif(opt=='q'):
                break
            elif(opt=='r'):
                opt=self.opts.pop()
                print('Undoing operation ',opt)
                self.snapshots.pop()
                self.matrix=self.snapshots[len(self.snapshots)-1]
                print((self.matrix))
                print("remaining operations: \n",self.opts)
            
            elif(opt=='opts'):
                print(self.opts)
            elif opt=='snaps':
                pprint(self.snapshots)
                
            else:
                print("unknown command!")


if __name__=='__main__':
    mat=FuzzyMatrix([[1,2,-3,3],[2,-1,-1,11],[3,2,1,-5]])
    mat.operate_rows()