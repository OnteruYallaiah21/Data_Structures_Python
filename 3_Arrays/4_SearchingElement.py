#it is done in a way linear search 
import array
arr1=array.array('i',[3,4,5,6,7,8])
def searching_Element(array,searchNum):
    exp1 =0
    for i in range(len(array)):
        if(searchNum==array[i]):
           # print("Yes The number is the Array")
            exp1=1
        else:
           exp1=0 
    if(exp1==1):
       print("Yes The number is the Array")
    else:
        print("The number is not present in the array")
 
          
searching_Element(arr1,8)
searching_Element(arr1,98)
    