def recursive(n):
     if n<=0:
        return n 
     return n+recursive(n-1)
recursive(3)
 #1=3+2=5,4,1