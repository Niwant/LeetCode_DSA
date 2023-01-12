
#User function Template for python3

class Solution:
    
    #Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self,s):
        #code here
        dict = {}
        
        for x in s:
            if x in dict:
                dict[x]+=1
            else:
                dict[x]=1
        m = s[0] 
        for x in dict.keys():
            if dict[x] >dict[m]:
                m=x
            elif  dict[x]== dict[m] and x<m:
                m=x
                
        return m 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        print(Solution().getMaxOccurringChar(s))
# } Driver Code Ends