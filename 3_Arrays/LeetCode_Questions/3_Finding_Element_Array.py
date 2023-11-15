#import numpy as np
#Liner Search
arra=[1,2,3,4,5,6,7,8,356,56554,645643];
def search_Element(arr,num):
    print("the array is "+str(arr)+"\nThe Searching Element Is =>"+str(num))
    for x in range(len(arr)):
        #print(x)
        if(arr[x]==num):
         return "Yes I found the Number";
        
    return "No element is Not Found"    
searrch_Element=int(input("enter the Roll Number You Need to find Out=>"));
print(search_Element(arra,searrch_Element));       

    
    