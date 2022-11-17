'''
Created on Nov 17, 2022

@author: mahalymarcelin
'''

# entry point test code; test solution class for leetcode problem 415.
# solution provided by Professor

from solutionPackage.Solution import *

mySolution = Solution()

result = mySolution.addStrings("69", "420")
print(result)

fail = mySolution.addStrings("aa3", "cock")
print(fail)