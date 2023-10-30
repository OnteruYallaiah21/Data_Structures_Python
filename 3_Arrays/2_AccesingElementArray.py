import array
arry1=array.array('i',[1,2,3,4,5,6,7])
print("It is soUt of Function Print Function",arry1[0])
def accesing_Element(array,index):
    if index>=len(array):
        print("This is not Element is accesing from this array")
    else:
        print(array[index])
print(accesing_Element(arry1,90))
    